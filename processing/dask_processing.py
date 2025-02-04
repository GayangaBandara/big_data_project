import dask.dataframe as dd

df = dd.read_csv("../data/raw/products.csv")
df = df.dropna()
df.to_csv("../data/processed/cleaned_data.csv", single_file=True)

print("Dask processing completed!")
