from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["big_data_project"]
collection = db["amazon_reviews"]

df = pd.read_csv("../data/raw/products.csv")
collection.insert_many(df.to_dict("records"))
print("Data stored in MongoDB successfully!")
