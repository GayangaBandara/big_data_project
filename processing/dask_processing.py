import dask.dataframe as dd

df = dd.read_csv("../data/raw/products.csv")
df = df.dropna()
<<<<<<< HEAD
df.to_csv("../data/processed/cleaned_data.csv", single_file=True)
=======
df.to_csv("../data/processed/part-00000-55078bd3-eca0-4078-8064-721c27ee24fc-c000.csv", single_file=True)
>>>>>>> 796738e (Dashbord Update)

print("Dask processing completed!")
