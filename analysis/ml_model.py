import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("../data/processed/part-00000-55078bd3-eca0-4078-8064-721c27ee24fc-c000.csv.csv")

# Select features and target variable
X = df[['likes', 'total_replies']]  # Features
y = df['comment_length']  # Target variable

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
pickle.dump(model, open("app/model.pkl", "wb"))
print("✅ Model training completed and saved as model.pkl!")
