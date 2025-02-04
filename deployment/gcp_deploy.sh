gsutil cp ../data/processed/cleaned_data.csv gs://your_bucket_name/
gcloud dataproc jobs submit pyspark processing/spark_processing.py --cluster=your-cluster
