# /app/feast_repo/customer_fv.py
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Int64, String

customer = Entity(name="customer_id", join_keys=["customer_id"])

src = FileSource(path="app/feast_repo/data/customers.csv", timestamp_field="event_timestamp")

customer_features = FeatureView(         # <-- name MUST be exactly "customer_features"
    name="customer_features",
    entities=[customer],
    schema=[Field(name="segment", dtype=String), Field(name="age", dtype=Int64)],
    online=True,
    source=src,
)
