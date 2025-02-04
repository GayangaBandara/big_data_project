#!/bin/bash

# Create HDFS directories
hdfs dfs -mkdir -p /big data project/raw
hdfs dfs -mkdir -p /big data project/processed

# Upload raw data to HDFS
hdfs dfs -put ../data/raw/*.csv /big data project/raw/products.csv

# Check HDFS directories
hdfs dfs -ls /big data project/raw/products.csv

echo "✅ HDFS setup completed successfully!"
