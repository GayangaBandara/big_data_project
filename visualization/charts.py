import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("../data/processed/cleaned_data.csv")

sns.boxplot(x=df["Category"], y=df["Price"])
plt.xticks(rotation=90)
plt.title("Product Category vs Price")
plt.show()
