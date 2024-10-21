# Databricks notebook source
# Create the volume first
spark.sql("CREATE VOLUME IF NOT EXISTS main.default.babynames")

# Now create the directory and upload the file
response = requests.get('http://health.data.ny.gov/api/views/jxy9-yhdk/rows.csv')
csvfile = response.content.decode('utf-8')

dbutils.fs.mkdirs("/Volumes/main/default/babynames")
dbutils.fs.put("/Volumes/main/default/babynames/babynames.csv", csvfile, True)
