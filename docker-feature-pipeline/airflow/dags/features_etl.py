from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import os
import pandas as pd
from sqlalchemy import create_engine
import subprocess

OFFLINE_URI = "postgresql+psycopg2://feast:feast@postgres:5432/feast_offline"
CSV_PATH = "/opt/airflow/dags/data/customers.csv"  # we'll copy a sample there

def load_and_aggregate():
    df = pd.read_csv(CSV_PATH)
    # Expect columns: customer_id, order_id, amount, event_timestamp
    df['event_timestamp'] = pd.to_datetime(df['event_timestamp'])
    agg = df.groupby('customer_id').agg(
        total_orders=('order_id', 'nunique'),
        avg_order_value=('amount', 'mean'),
        event_timestamp=('event_timestamp', 'max'),
    ).reset_index()
    engine = create_engine(OFFLINE_URI)
    with engine.begin() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS public.customer_features(
              customer_id BIGINT,
              total_orders BIGINT,
              avg_order_value DOUBLE PRECISION,
              event_timestamp TIMESTAMP
            );
        """)
        agg.to_sql("customer_features", conn, schema="public", if_exists="replace", index=False)

def feast_apply():
    # Run feast apply inside the webserver container's mounted repo
    subprocess.check_call(["feast", "-c", "/opt/airflow/dags/../../feast_repo", "apply"])

def feast_materialize():
    # Materialize last 30 days into Redis
    now = datetime.utcnow()
    start = (now - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%S")
    end = now.strftime("%Y-%m-%dT%H:%M:%S")
    subprocess.check_call([
        "feast", "-c", "/opt/airflow/dags/../../feast_repo", "materialize",
        start, end
    ])

with DAG(
    dag_id="features_etl",
    start_date=datetime(2025, 10, 1),
    schedule="@daily",
    catchup=False,
    default_args={"retries": 1, "retry_delay": timedelta(seconds=15)},
) as dag:

    t1 = PythonOperator(task_id="load_aggregate_to_postgres", python_callable=load_and_aggregate)
    t2 = PythonOperator(task_id="feast_apply_definitions", python_callable=feast_apply)
    t3 = PythonOperator(task_id="feast_materialize_to_redis", python_callable=feast_materialize)

    t1 >> t2 >> t3
