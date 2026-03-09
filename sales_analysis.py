import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("C:\Users\HP\Downloads\sales_data.csv")

# Total sales
print("Total Sales:", data["Sales"].sum())

# Sales by Region
region_sales = data.groupby("Region")["Sales"].sum()
print(region_sales)

# Plot
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.show()
