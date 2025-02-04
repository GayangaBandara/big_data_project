from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

# Initialize Spark Session
spark = SparkSession.builder.appName("YouTubeCommentsProcessing").getOrCreate()

# Load JSON file
json_path = "youtube_comments.json"  # Update path if needed
df = spark.read.option("multiline", "true").json(json_path)

# Extract relevant fields
df_cleaned = df.select(
    col("author").alias("author"),
    col("comment").alias("comment"),
    col("likes").alias("likes"),
    col("published_at").alias("published_at"),
    col("total_replies").alias("total_replies")
)

# Remove rows with missing values
df_cleaned = df_cleaned.dropna()

# Optional: Filter out comments that are too short or contain only emojis
df_cleaned = df_cleaned.filter(expr("length(comment) > 5"))

# Save processed data as CSV
output_path = "processed_youtube_comments.csv"
df_cleaned.write.csv(output_path, header=True)

print("✅ YouTube comments processed and saved as CSV!")
