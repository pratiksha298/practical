import pandas as pd
df = pd.read_csv('Tennis.csv')
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Encoding categorical data
le = LabelEncoder()
for column in df.columns:
    df[column] = le.fit_transform(df[column])

X = df.drop('play', axis=1)
y = df['play']

clf = DecisionTreeClassifier()
clf.fit(X, y)

print("Decision Tree Accuracy:", clf.score(X, y))
