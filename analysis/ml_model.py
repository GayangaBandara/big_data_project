import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

<<<<<<< HEAD
df = pd.read_csv("../data/processed/cleaned_data.csv")
=======
df = pd.read_csv("../data/processed/part-00000-55078bd3-eca0-4078-8064-721c27ee24fc-c000.csv.csv")
>>>>>>> 796738e (Dashbord Update)

X = df[['Feature1', 'Feature2']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

pickle.dump(model, open("../app/model.pkl", "wb"))
print("Model training completed!")
