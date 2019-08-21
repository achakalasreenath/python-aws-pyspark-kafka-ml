from pyspark.sql import SparkSession
import pyspark.sql.functions as func

spark_session = SparkSession.builder.appName('Analysing London Crimes').getOrCreate()


def read_data(filename):
    return spark_session.read.format("csv").option("header", "true").load(filename)


if __name__ == "__main__":
    data = read_data(r'C:\Users\achakala.sreenath\PycharmProjects\spark2\demo\datasets\london_crime_by_lsoa.csv')
    convictions_per_borough = data.groupBy("borough").agg({"value": "sum"}).withColumnRenamed("sum(value)",
                                                                                              "convictions")
    total_convictions = convictions_per_borough.agg({"convictions": "sum"})
    percentage_contribution_data_of_borough = convictions_per_borough.withColumn("percentage_contribution", func.round(
        (convictions_per_borough["convictions"] / total_convictions.collect()[0][0]) * 100, 2))

    convictions_per_month = data.groupBy("month").agg({"value": "sum"}).withColumnRenamed("sum(value)"
                                                                                          , "convictionsmonthly")
    total_convictions_per_month = convictions_per_month.agg({"convictionsmonthly": "sum"})
    percentage_contribution_per_month = convictions_per_month.withColumn("percentage_contribution", func.round(
        (convictions_per_month["convictionsmonthly"] / total_convictions_per_month.collect()[0][0]) * 100, 2))

    #orderBy
    descending_percentage_contribution = percentage_contribution_per_month.orderBy(percentage_contribution_per_month.percentage_contribution.desc())
