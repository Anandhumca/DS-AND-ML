
import pandas as pd

# Read the Chipotle dataset
df = pd.read_csv("chipotle.csv")


# a) Display first 5 rows
print("First 5 rows:")
print(df.head())


# b) Sort item_price in descending order
# Convert item_price to float
# This works whether the CSV contains $ or not
df["item_price"] = (
    df["item_price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .astype(float)
)

sorted_df = df.sort_values("item_price", ascending=False)

print("\nFirst 5 rows after sorting by item_price:")
print(sorted_df.head())


# c) Display records where item_name contains "chicken"
chicken = df[
    df["item_name"].str.contains("chicken", case=False, na=False)
]

print("\nRecords containing 'chicken':")
print(chicken)


# d) Remove square brackets from choice_description
df["choice_description"] = df["choice_description"].astype(str).str.replace(
    r"[\[\]]", "", regex=True
)

print("\nChoice description after removing square brackets:")
print(df["choice_description"].head())


# e) Display datatype of each column
print("\nData types of each column:")
print(df.dtypes)


# f) Display item_price after removing $ and converting to float
print("\nItem price after converting to float:")
print(df["item_price"].head())

print("\nDatatype of item_price:")
print(df["item_price"].dtype)

