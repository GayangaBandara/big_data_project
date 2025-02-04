#!/bin/bash

# Create HDFS directories
hdfs dfs -mkdir -p /big_data_project/raw
hdfs dfs -mkdir -p /big_data_project/processed

# Upload raw data to HDFS
hdfs dfs -put ../data/raw/*.csv /big_data_project/raw/

# Check HDFS directories
hdfs dfs -ls /big_data_project/

echo "✅ HDFS setup completed successfully!"
