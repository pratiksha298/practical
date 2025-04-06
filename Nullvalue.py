import pandas as pd
from sklearn.impute import SimpleImputer
df = pd.read_csv('iris.csv')
print("Null values in dataset before filling:")
print(df.isnull().sum())
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
imputer = SimpleImputer(strategy='mean')
df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
print("\nNull values in dataset after filling:")
print(df.isnull().sum())