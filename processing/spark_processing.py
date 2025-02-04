from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder.appName("YouTubeCommentsProcessing").getOrCreate()

# Load JSON file
json_path = "../data/raw/youtube_comments.json"  # Update path if needed
df = spark.read.option("multiline", "true").json(json_path)

# Extract relevant fields
df_extracted = df.selectExpr("explode(items) as item")
df_cleaned = df_extracted.select(
    col("item.snippet.videoId").alias("video_id"),
    col("item.snippet.topLevelComment.snippet.authorDisplayName").alias("author"),
    col("item.snippet.topLevelComment.snippet.textOriginal").alias("comment"),
    col("item.snippet.topLevelComment.snippet.likeCount").alias("likes"),
    col("item.snippet.topLevelComment.snippet.publishedAt").alias("published_at")
)

# Remove rows with missing values
df_cleaned = df_cleaned.dropna()

# Save processed data as CSV
output_path = "../data/processed/youtube_comments.csv"
df_cleaned.write.csv(output_path, header=True)

print("✅ YouTube comments processed and saved as CSV!")
