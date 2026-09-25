import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

df = pd.read_csv("data/orders_clustered.csv")

features = [
    "distance_km",
    "delivery_zone",
    "hour_of_day",
    "parcel_volume",
    "traffic_index"
]

X = df[features]
y = df["delivery_delay_min"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = GradientBoostingRegressor(
    n_estimators=300,
    max_depth=4,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(
    y_test,
    predictions
) ** 0.5
r2 = r2_score(y_test, predictions)

print("Gradient Boosting Results")
print("-------------------------")
print("MAE :", round(mae, 2), "minutes")
print("RMSE:", round(rmse, 2), "minutes")
print("R2  :", round(r2, 3))

plt.figure(figsize=(8, 6))

plt.scatter(
    y_test,
    predictions,
    alpha=0.6
)

lims = [
    min(y_test.min(), predictions.min()),
    max(y_test.max(), predictions.max())
]

plt.plot(lims, lims, "--")

plt.xlabel("Actual Delay (minutes)")
plt.ylabel("Predicted Delay (minutes)")
plt.title("Actual vs Predicted Delivery Delay")
plt.tight_layout()
plt.savefig("delay_prediction.png", dpi=180)
plt.show()
