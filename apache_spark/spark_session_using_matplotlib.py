from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

spark_session = SparkSession.builder.appName('Analysing London Crimes').getOrCreate()


def read_data(filename):
    return spark_session.read.format("csv").option("header", "true").load(filename)


def describe(year, data):
    year_details = data.filter(data.year == year).groupBy("borough").agg({"value": "sum"})
    borough_list = [x[0] for x in year_details.toLocalIterator()]
    major_category_list = [x[1] for x in year_details.toLocalIterator()]
    plt.figure(figsize=(33, 10))
    plt.bar(borough_list, major_category_list)
    plt.title("crimes for the year {}".format(year))
    plt.xlabel("Borough", fontsize=30)
    plt.ylabel("major_category", fontsize=30)
    plt.xticks(rotation=90,fontsize = 10)
    plt.yticks(fontsize=10)
    plt.autoscale()
    plt.show()


if __name__ == "__main__":
    data = read_data(r'C:\Users\achakala.sreenath\PycharmProjects\spark2\demo\datasets\london_crime_by_lsoa.csv')
    convictions_per_category = data.groupBy("major_category").agg({"value": "sum"}).withColumnRenamed("sum(value",
                                                                                                      "convictions")
    # data_in_matrix_form
    # this adds a column "borough_major_category" in the dataframe
    convictions_in_a_borough_in_each_category = data.crosstab("borough", 'major_category')
    describe(2014,data)
