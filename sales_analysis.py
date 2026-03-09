import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# Total Sales
print("Total Sales:", data["Sales"].sum())

# Sales by Region
region_sales = data.groupby("Region")["Sales"].sum()
print(region_sales)

plt.figure(figsize=(6,4))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.savefig("sales_by_region.png")
plt.show()

# Sales by Product
product_sales = data.groupby("Product")["Sales"].sum()

plt.figure(figsize=(6,4))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.savefig("sales_by_product.png")
plt.show()

# Sales Distribution
plt.figure(figsize=(6,4))
sns.histplot(data["Sales"], bins=5)
plt.title("Sales Distribution")
plt.savefig("sales_distribution.png")
plt.show()
