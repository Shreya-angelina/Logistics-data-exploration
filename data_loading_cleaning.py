import pandas as pd
import numpy as np

orders = pd.read_csv(
    "data/orders.csv",
    parse_dates=["order_time", "promised_time", "delivery_time"]
)

telemetry = pd.read_csv("data/vehicle_telemetry.csv")

orders = orders.drop_duplicates(subset="order_id")

orders["delivery_delay_min"] = (
    orders["delivery_time"] - orders["promised_time"]
).dt.total_seconds() / 60

orders = orders.dropna(
    subset=["origin_hub", "destination_lat", "destination_lon"]
)

orders["hour_of_day"] = orders["order_time"].dt.hour

orders["is_late"] = orders["delivery_delay_min"] > 0

orders.to_csv("data/orders_cleaned.csv", index=False)

print("Cleaned dataset shape:", orders.shape)
print("\nMissing values:")
print(orders.isnull().sum())
print("\nSaved: data/orders_cleaned.csv")
