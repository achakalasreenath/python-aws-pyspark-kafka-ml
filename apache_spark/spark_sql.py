from pyspark.sql import SparkSession

spark_session = SparkSession.builder.appName("analysing airline data").getOrCreate()

