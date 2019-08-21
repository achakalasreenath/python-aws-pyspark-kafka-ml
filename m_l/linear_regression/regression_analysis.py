from pyspark.sql import SparkSession
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sl
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import array

spark_session = SparkSession.builder.appName("analysis of weather dataset for linear regression").getOrCreate()
dataset = spark_session.read.format("csv").option("header", "true").load(
    r'm_l/datasets/Weather.csv')

def plot_data(dataset):
    plt.figure(figsize=(33,10))
    min_temp = [x["MinTemp"] for x in dataset.toLocalIterator()]
    max_temp = [x["MaxTemp"] for x in dataset.toLocalIterator()]
    plt.plot(min_temp,max_temp,'bo')
    plt.xlabel("MinTemp")
    plt.ylabel("MaxTemp")
    plt.xticks(rotation = 90,fontsize=10)
    plt.yticks(fontsize=10)
    plt.autoscale()
    plt.show()

def model(dataset):
    min_temp = [float(x["MinTemp"]) for x in dataset.toLocalIterator()]
    max_temp = [float(x["MaxTemp"]) for x in dataset.toLocalIterator()]
    X = np.array(min_temp).reshape(-1, 1)
    Y = np.array(max_temp).reshape(-1, 1)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state = 0)
    model = LinearRegression()
    model.fit(X_train,Y_train)
    result = model.score(X_test,Y_test)
    y_pred = model.predict(Y_test)
    plt.plot(Y_test,y_pred,'.')
    return result
