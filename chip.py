import pandas as pd

# Read the Chipotle dataset
df = pd.read_csv("chipotle.csv")


# a) Display first 5 rows
print("First 5 rows:")
print(df.head())


# b) Sort item_price in descending order
# First remove $ and convert item_price to float
df["item_price"] = df["item_price"].str.replace("$", "", regex=False)
df["item_price"] = df["item_price"].astype(float)

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
df["choice_description"] = df["choice_description"].str.replace(
    r"[\[\]]", "", regex=True
)

print("\nChoice description after removing square brackets:")
print(df["choice_description"].head())


# e) Display datatype of each column
print("\nData types of each column:")
print(df.dtypes)


# f) Replace $ and convert item_price to float
# Already done above

print("\nItem price after converting to float:")
print(df["item_price"].head())

print("\nDatatype of item_price:")
print(df["item_price"].dtype)