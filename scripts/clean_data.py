import pandas as pd

# Read the raw dataframe
df = pd.read_csv("data/raw_data.csv")

# Check missing values per column
print("Missing values:")
print(df.isna().sum())

# Drop rows with missing Store_ID
# Create a new dataframe so the raw dataframe is not modified
df_clean = df.dropna(subset=["Store_ID"]).copy()

print("\nAfter dropping missing Store_ID:")
print(df_clean.isna().sum())

# Fill missing Revenue using the median Revenue
# of the corresponding Units_Sold group
df_clean["Revenue"] = df_clean["Revenue"].fillna(
    df_clean.groupby("Units_Sold")["Revenue"].transform("median")
)

# If any Revenue values are still missing,
# fill them with the overall median
df_clean["Revenue"] = df_clean["Revenue"].fillna(
    df_clean["Revenue"].median()
)

print("\nAfter imputing missing Revenue:")
print(df_clean.isna().sum())

# Save cleaned dataframe
df_clean.to_csv("data/clean_data.csv", index=False)


