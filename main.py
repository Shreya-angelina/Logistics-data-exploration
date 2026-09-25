"""
Week 1 Logistics Strategic Planning Pipeline

Run this file to execute the main stages:
1. Data loading and cleaning
2. Exploratory data analysis
3. Delivery-zone clustering
4. Delay-risk prediction
5. Route planning
6. Inventory allocation

The individual scripts can also be run separately.
"""

import subprocess
import sys

scripts = [
    "data_loading_cleaning.py",
    "eda.py",
    "cluster_zones.py",
    "predictive_model.py",
    "route_optimization.py",
    "inventory_optimization.py"
]

for script in scripts:
    print("\n" + "=" * 60)
    print("Running:", script)
    print("=" * 60)

    subprocess.run(
        [sys.executable, script],
        check=True
    )

print("\nWeek 1 pipeline completed successfully.")
