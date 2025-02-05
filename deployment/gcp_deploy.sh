<<<<<<< HEAD
gsutil cp ../data/processed/cleaned_data.csv gs://your_bucket_name/
=======
gsutil cp ../data/processed/part-00000-55078bd3-eca0-4078-8064-721c27ee24fc-c000.csv.csv gs://your_bucket_name/
>>>>>>> 796738e (Dashbord Update)
gcloud dataproc jobs submit pyspark processing/spark_processing.py --cluster=your-cluster
