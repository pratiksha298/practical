import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("iris.csv")
plt.scatter(df['sepal_length'], df['petal_length'], color='green')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.title('Scatter Plot of Sepal Length vs Petal Length')
plt.show()
