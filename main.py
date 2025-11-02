import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

sns.histplot(df['price'], kde=True)
plt.title('Car Price Distribution')
plt.show()

sns.boxplot(x='fuel_type', y='price', data=df)
plt.title('Fuel Type vs Price')
plt.show()
