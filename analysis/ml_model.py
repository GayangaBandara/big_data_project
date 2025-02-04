import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("../data/processed/cleaned_data.csv")

X = df[['Feature1', 'Feature2']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

pickle.dump(model, open("../app/model.pkl", "wb"))
print("Model training completed!")
