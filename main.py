import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


df= pd.read_csv("data/car_price_data.csv")
# ========================CHECK DATA =============================
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
#----------------- SEABORN AND MATPLOTLIB-------------------
# sns.histplot(df['price'], kde=True)
# plt.title('Car Price Distribution')
# plt.show()

# sns.boxplot(x='fuel_type', y='price', data=df)
# plt.title('Fuel Type vs Price')
# plt.show()

#========================= DATA PROCESSING =========================

# Check total missing values in each column
print("Missing Values in Each Column:")
print(df.isnull().sum())

#================= DATA ENCODING =================
le = LabelEncoder()

for col in df.select_dtypes(include=['object']).columns:
    df[col] = le.fit_transform(df[col])

print("✅ Encoding completed successfully!")
print(df.dtypes.head())  