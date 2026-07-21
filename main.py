from src.load_data import load_data
from src.clean_data import (
    clean_data,
    columns_cleaning,
    new_cols,
    del_cols
)

df = load_data("data/raw/customer_shopping_behavior.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe(include="all"))
print(df.columns)
print(df.duplicated().sum())
print(df.isnull().sum())

df = columns_cleaning(df)
df = clean_data(df)
df = new_cols(df)
df = del_cols(df)
df.to_csv("data/cleaned/cleaned_sales.csv", index=False)
print(df.isnull().sum())
print(df[['age','age_group']].head(10))
print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))

