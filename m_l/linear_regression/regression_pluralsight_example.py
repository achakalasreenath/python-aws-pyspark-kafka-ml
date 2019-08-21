import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import round, monotonically_increasing_id
from pyspark.sql.types import StructField, StructType, DoubleType, FloatType, IntegerType, StringType, BinaryType, \
    LongType, ArrayType
from sklearn import preprocessing
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

spark_session = SparkSession.builder.appName("data preperation for machine learning modelling").getOrCreate()
dataset = spark_session.read.format("csv").option("header", "true").load(
    r'm_l/datasets/weatherHistory.csv')
sql_context = pyspark.sql.SQLContext(spark_session)

# preprocessing
dataset = dataset.toPandas()
dataset["Temperature (C)"] = preprocessing.scale(dataset["Temperature (C)"])
dataset["Humidity"] = preprocessing.scale(dataset["Humidity"])
# converting from object type to float type
dataset["Pressure (millibars)"] = pd.to_numeric(dataset["Pressure (millibars)"],errors = "coerce")
dataset["Pressure (millibars)"] = preprocessing.scale(dataset["Pressure (millibars)"])


dataset = dataset.drop(["Formatted Date","Loud Cover","Apparent Temperature (C)","Wind Speed (km/h)","Wind Bearing (degrees)","Visibility (km)", "Precip Type"], axis=1)
# one hot encoding of text data
dataset = pd.get_dummies(dataset, columns=["Summary", "Daily Summary"])

# replacing missing values with mean in a column
simp_imp = SimpleImputer(strategy='mean', missing_values=np.nan)
dataset["Temperature (C)"] = simp_imp.fit_transform(dataset.values)
dataset = dataset.dropna()


Y = pd.to_numeric(dataset["Humidity"],errors = "coerce")
X = dataset.drop(["Humidity"],axis =1)

# defining a Linear Regression Model
model = LinearRegression()

# splitting training data and test data
X_train, x_test, Y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=0)

# generating a fitting model
model_fit = model.fit(X_train, Y_train)

# predicting with test data
y_pred = model.predict(x_test)

# R sqaure value to measure the accuracy of our prediction
print(model.score(X_train,Y_train))
print(model.score(x_test,y_test))

# plot between predicted values and actual values
plt.plot(y_pred[1:10],label = "predicted")
plt.plot(y_test[1:10],label = "actual")
plt.legend()
plt.show()