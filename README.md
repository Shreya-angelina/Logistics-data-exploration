# Week 1 – Strategic Planning & Data Exploration in Logistics

This repository contains the Python implementation for the Week 1 logistics project based on the Northbridge Logistics scenario.

## Project Objective

The project explores how historical logistics data can be used to:

- Improve On-Time Delivery Rate (OTDR)
- Reduce Cost per Delivery (CPD)
- Reduce inventory stockouts
- Improve vehicle utilization
- Reduce order fulfillment cycle time

## Program Files

- `generate_data.py` – Generates representative logistics order and telemetry data.
- `data_loading_cleaning.py` – Loads and cleans the operational datasets.
- `eda.py` – Performs exploratory analysis of delays, cost, distance and hub-level performance.
- `cluster_zones.py` – Uses K-Means to segment delivery locations into geographic zones.
- `predictive_model.py` – Uses Gradient Boosting Regression to predict delivery delay.
- `route_optimization.py` – Creates capacity-aware delivery route groupings for each delivery zone.
- `inventory_optimization.py` – Uses Linear Programming through SciPy to allocate inventory across hubs.
- `main.py` – Runs the complete pipeline.
- `requirements.txt` – Required Python packages.

## Analytical Roadmap

The implementation follows the roadmap described in the project report:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Delivery Zone Clustering
6. Predictive Modeling
7. Route and Inventory Optimization
8. Evaluation and Reporting

## Run the Project

```bash
pip install -r requirements.txt
python generate_data.py
python main.py
```

Individual programs can also be executed separately.

## Main Techniques

- Pandas and NumPy
- Matplotlib and Seaborn
- K-Means Clustering
- Gradient Boosting Regression
- SciPy Linear Programming
- Capacity-aware route grouping

The dataset in this repository is representative/simulated for demonstrating the analytical roadmap before proprietary Northbridge Logistics data is available.
