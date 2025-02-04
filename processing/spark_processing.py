from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BigDataProject").getOrCreate()
df = spark.read.csv("../data/raw/products.csv", header=True, inferSchema=True)

df = df.dropna()  # Remove missing values
df.write.csv("../data/processed/cleaned_data.csv", header=True)

print("Data processing completed!")
