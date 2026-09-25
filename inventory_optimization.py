import numpy as np
import pandas as pd
from scipy.optimize import linprog

# Example forecasted demand for the three hubs.
hubs = ["Hub 1", "Hub 2", "Hub 3"]

forecasted_demand = np.array([
    4200,
    3600,
    3000
])

hub_capacity = np.array([
    6000,
    5000,
    4500
])

holding_cost = np.array([
    2.0,
    2.2,
    2.1
])

shortage_penalty = np.array([
    8.0,
    8.5,
    8.2
])

# Objective: holding cost + shortage penalty.
c = holding_cost + shortage_penalty

# x represents inventory allocated to each hub.
# Each hub must receive at least its forecast demand.
A_ub = np.eye(3)
b_ub = hub_capacity

A_eq = np.ones((1, 3))
b_eq = [sum(forecasted_demand)]

result = linprog(
    c=c,
    A_ub=A_ub,
    b_ub=b_ub,
    A_eq=A_eq,
    b_eq=b_eq,
    bounds=(0, None),
    method="highs"
)

if not result.success:
    raise RuntimeError(result.message)

allocation = pd.DataFrame({
    "Hub": hubs,
    "ForecastedDemand": forecasted_demand,
    "Capacity": hub_capacity,
    "OptimizedAllocation": result.x.round(2)
})

print("Inventory Allocation:")
print(allocation.to_string(index=False))

allocation.to_csv(
    "data/inventory_allocation.csv",
    index=False
)

print("\nSaved: data/inventory_allocation.csv")
