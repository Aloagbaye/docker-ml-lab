from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, Int64
from feast import PushSource
from datetime import timedelta

customer = Entity(name="customer_id", join_keys=["customer_id"])

# Offline source: a Postgres table we'll create via Airflow DAG (public.customer_features)
from feast.infra.offline_stores.contrib.postgres_offline_store.postgres_source import PostgreSQLSource

offline_source = PostgreSQLSource(
    name="customer_features_offline",
    query="SELECT customer_id, total_orders, avg_order_value, event_timestamp FROM public.customer_features",
    timestamp_field="event_timestamp",
)

customer_fv = FeatureView(
    name="customer_features",
    entities=[customer],
    ttl=timedelta(days=7),
    schema=[
        Field(name="total_orders", dtype=Int64),
        Field(name="avg_order_value", dtype=Float32),
    ],
    online=True,
    source=offline_source,
)
