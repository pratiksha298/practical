import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
data = pd.read_csv("Position_Salaries.csv")
X = data.iloc[:, 1:2].values  
y = data.iloc[:, 2].values    
poly = PolynomialFeatures(degree=3)  
X_poly = poly.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, y)
y_pred = model.predict(X_poly)
plt.scatter(X, y, color='red', label="Actual")
plt.plot(X, y_pred, color='blue', label="Polynomial Regression")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.legend()
plt.show()
