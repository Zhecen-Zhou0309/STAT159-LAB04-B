import pandas as pd

# Read the raw dataframe
df = pd.read_csv("data/raw_data.csv")

# Check missing values per column
print("Missing values:")
print(df.isna().sum())

# Create a new clean dataframe and drop rows with missing Store_ID
df_clean = df.dropna(subset=["Store_ID"]).copy()

# Save the cleaned dataframe
df_clean.to_csv("data/clean_data.csv", index=False)

print("\nAfter dropping missing Store_ID:")
print(df_clean.isna().sum())


