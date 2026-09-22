import pandas as pd

# Read the processed dataframe
df = pd.read_csv("data/processed_data.csv")

# Create store summary
store_summary = df.groupby("Store_ID").agg(
    total_revenue=("Revenue", "sum"),
    avg_units_sold=("Units_Sold", "mean"),
    unique_order_segments=("order_segment", "nunique")
)

# Calculate IQR for Revenue
Q1 = df["Revenue"].quantile(0.25)
Q3 = df["Revenue"].quantile(0.75)
IQR = Q3 - Q1

upper_bound = Q3 + 1.5 * IQR

# Identify high-revenue outliers
outliers = df[df["Revenue"] > upper_bound]

# Print results
print("Store Summary:")
print(store_summary)

print("\nRevenue Outliers:")
print(outliers)

# Save results to a text file
with open("results/summary.txt", "w") as f:
    f.write("Store Summary:\n")
    f.write(store_summary.to_string())

    f.write("\n\nRevenue Outliers:\n")
    f.write(outliers.to_string(index=False))
