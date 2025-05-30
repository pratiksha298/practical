import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
df = pd.read_csv("kc_house_data.csv")
y = df['price']
def train_and_plot(X, title, subplot):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression().fit(X_train, y_train)
    y_pred = model.predict(X_test)    
    print(f"\n{title}:\nMAE: {mean_absolute_error(y_test, y_pred)}\nMSE: {mean_squared_error(y_test, y_pred)}\nR2: {r2_score(y_test, y_pred)}")
    plt.subplot(1, 2, subplot)
    plt.scatter(X_test.iloc[:, 0], y_test, color='blue', label='Actual salaries')
    plt.scatter(X_test.iloc[:, 0], y_pred, color='red', label='Predicted')
    plt.xlabel(X.columns[0])
    plt.ylabel("Price")
    plt.title(title)
    plt.legend()
plt.figure(figsize=(12, 5))
train_and_plot(df[['sqft_living']], "Simple Linear Regression", 1)
train_and_plot(df[['sqft_living', 'bedrooms', 'bathrooms', 'floors', 'sqft_lot']], "Multiple Linear Regression", 2)
plt.tight_layout()
plt.show()
