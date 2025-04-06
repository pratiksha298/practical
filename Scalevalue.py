import pandas as pd
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("Salary_Data.csv")
print("Original Dataset:\n", df.head())
scaler = StandardScaler()
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
print("\nStandardized Dataset:\n", df.head())