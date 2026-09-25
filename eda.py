import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "data/orders_cleaned.csv",
    parse_dates=["order_time", "promised_time", "delivery_time"]
)

print("Dataset shape:", df.shape)

print("\nSummary statistics:")
print(df.describe())

print("\nAverage delay by hub:")
print(
    df.groupby("origin_hub")["delivery_delay_min"]
    .mean()
)

print("\nAverage cost by hub:")
print(
    df.groupby("origin_hub")["delivery_cost"]
    .mean()
)

print("\nCorrelation:")
print(
    df[[
        "distance_km",
        "traffic_index",
        "parcel_volume",
        "delivery_delay_min",
        "delivery_cost"
    ]].corr()
)

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="origin_hub",
    y="delivery_delay_min"
)
plt.title("Delivery Delay Distribution by Hub")
plt.xlabel("Origin Hub")
plt.ylabel("Delay (minutes)")
plt.tight_layout()
plt.savefig("delay_by_hub.png", dpi=180)
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="distance_km",
    y="delivery_delay_min",
    hue="origin_hub"
)
plt.title("Distance vs Delivery Delay")
plt.tight_layout()
plt.savefig("distance_vs_delay.png", dpi=180)
plt.show()
