import pandas as pd
import numpy as np

df = pd.read_csv("data/orders_clustered.csv")

VAN_CAPACITY = 8
MAX_STOPS_PER_ROUTE = 10

optimized_routes = []

for zone in sorted(df["delivery_zone"].unique()):

    zone_data = df[
        df["delivery_zone"] == zone
    ].copy()

    # Simple nearest-neighbour style ordering using
    # distance from the zone centroid.
    center_lat = zone_data["destination_lat"].mean()
    center_lon = zone_data["destination_lon"].mean()

    zone_data["distance_from_center"] = np.sqrt(
        (zone_data["destination_lat"] - center_lat) ** 2
        + (zone_data["destination_lon"] - center_lon) ** 2
    )

    zone_data = zone_data.sort_values(
        "distance_from_center"
    )

    current_route = []
    current_load = 0

    for _, row in zone_data.iterrows():

        parcel = int(row["parcel_volume"])

        if (
            current_load + parcel > VAN_CAPACITY
            or len(current_route) >= MAX_STOPS_PER_ROUTE
        ):
            if current_route:
                optimized_routes.append({
                    "delivery_zone": zone,
                    "stops": current_route,
                    "vehicle_load": current_load
                })

            current_route = []
            current_load = 0

        current_route.append(row["order_id"])
        current_load += parcel

    if current_route:
        optimized_routes.append({
            "delivery_zone": zone,
            "stops": current_route,
            "vehicle_load": current_load
        })

routes = pd.DataFrame(optimized_routes)

print("Number of optimized routes:", len(routes))
print("\nFirst 10 routes:")
print(routes.head(10).to_string(index=False))

routes.to_csv(
    "data/optimized_routes.csv",
    index=False
)

print("\nSaved: data/optimized_routes.csv")
