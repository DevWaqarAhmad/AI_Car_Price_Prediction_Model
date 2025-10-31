import pandas as pd

df= pd.read_csv("data/car_price_data.csv")

print(df.head(3))
# print("Shape:", df.shape)

# print("\nInfo:")
# print(df.info())

# print("\nDescription:")
# print(df.describe())

# print("\nMISSING VALUES:")
# print(df.isnull().sum())


# print("\nUnique values in each column:")
# for col in df.columns:
#     print(f"{col}: {df[col].nunique()} unique")
