import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://example.com"
response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

data = []
for item in soup.find_all("div", class_="product"):
    name = item.find("h2").text
    price = item.find("span", class_="price").text
    data.append({"Name": name, "Price": price})

df = pd.DataFrame(data)
df.to_csv("../data/raw/products.csv", index=False)
print("Scraped data saved successfully!")
