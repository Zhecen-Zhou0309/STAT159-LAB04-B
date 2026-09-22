import pandas as pd
import numpy as np

# Read the cleaned dataframe
df_clean = pd.read_csv("data/clean_data.csv")

# Create unit price
df_clean["Unit_Price"] = (
    df_clean["Revenue"] / df_clean["Units_Sold"]
)

# Create order segment
conditions = [
    (df_clean["Revenue"] >= 300) & (df_clean["Units_Sold"] >= 5),
    (df_clean["Revenue"] >= 100),
    (df_clean["Revenue"] < 100)
]

choices = [
    "Bulk High-Value",
    "Standard Retail",
    "Low-Margin"
]

df_clean["order_segment"] = np.select(
    conditions,
    choices,
    default="Other"
)

# Inspect the new dataframe
print(df_clean.head())
print("\nOrder segment counts:")
print(df_clean["order_segment"].value_counts())

# Save the new dataframe
df_clean.to_csv("data/processed_data.csv", index=False)

