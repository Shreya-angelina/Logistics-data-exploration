import numpy as np
import pandas as pd

np.random.seed(42)

N = 1200

order_time = pd.date_range("2025-01-01", periods=N, freq="6h")
origin_hub = np.random.choice(["Hub 1", "Hub 2", "Hub 3"], N)

lat = np.random.uniform(12.85, 13.20, N)
lon = np.random.uniform(80.05, 80.35, N)

distance = np.random.uniform(2, 45, N)
parcel_volume = np.random.randint(1, 8, N)
traffic = np.clip(np.random.beta(4, 3, N), 0, 1)

hour = order_time.hour
promised_time = order_time + pd.to_timedelta(
    3 + distance / 12 + parcel_volume * 0.15, unit="h"
)

delay = (
    distance * 0.55
    + traffic * 25
    + parcel_volume * 1.5
    + np.random.normal(0, 5, N)
)

delivery_time = promised_time + pd.to_timedelta(
    np.maximum(delay, -10), unit="m"
)

cost = (
    45
    + distance * 4.2
    + parcel_volume * 8
    + traffic * 20
    + np.random.normal(0, 8, N)
)

orders = pd.DataFrame({
    "order_id": [f"ORD{100000+i}" for i in range(N)],
    "order_time": order_time,
    "promised_time": promised_time,
    "delivery_time": delivery_time,
    "origin_hub": origin_hub,
    "destination_lat": lat,
    "destination_lon": lon,
    "distance_km": distance.round(2),
    "parcel_volume": parcel_volume,
    "traffic_index": traffic.round(3),
    "delivery_cost": cost.round(2)
})

orders.to_csv("data/orders.csv", index=False)

# Vehicle telemetry
telemetry = pd.DataFrame({
    "order_id": orders["order_id"],
    "vehicle_id": np.random.choice(
        [f"V{i:03d}" for i in range(1, 121)], N
    ),
    "traffic_index": traffic.round(3)
})

telemetry.to_csv("data/vehicle_telemetry.csv", index=False)

print("Created data/orders.csv")
print("Created data/vehicle_telemetry.csv")
print("Records:", N)
