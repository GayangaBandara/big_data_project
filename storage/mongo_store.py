from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")

db = client["big data project"]
collection = db["amazon_reviews"]

df = pd.read_csv("../data/raw/products.csv")

db = client["bigdataproject"]
collection = db["amazon_reviews"]

df = pd.read_json("data/raw/youtube_comments.json")

collection.insert_many(df.to_dict("records"))
print("Data stored in MongoDB successfully!")
