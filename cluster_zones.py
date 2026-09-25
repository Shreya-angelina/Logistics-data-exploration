import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("data/orders_cleaned.csv")

coords = df[
    ["destination_lat", "destination_lon"]
].values

kmeans = KMeans(
    n_clusters=15,
    random_state=42,
    n_init=10
)

df["delivery_zone"] = kmeans.fit_predict(coords)

zone_summary = df.groupby("delivery_zone").agg(
    avg_delay=("delivery_delay_min", "mean"),
    parcel_count=("order_id", "count"),
    avg_distance=("distance_km", "mean")
).reset_index()

print("\nDelivery Zone Summary:")
print(zone_summary)

plt.figure(figsize=(9, 7))

plt.scatter(
    df["destination_lon"],
    df["destination_lat"],
    c=df["delivery_zone"],
    s=18,
    alpha=0.65
)

centers = kmeans.cluster_centers_

plt.scatter(
    centers[:, 1],
    centers[:, 0],
    marker="X",
    s=120
)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Delivery Zone Clustering using K-Means")
plt.tight_layout()
plt.savefig("delivery_zones.png", dpi=180)
plt.show()

df.to_csv(
    "data/orders_clustered.csv",
    index=False
)

print("\nSaved: data/orders_clustered.csv")
