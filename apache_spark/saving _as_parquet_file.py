from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast

spark_session = SparkSession.builder.appName("analysing soccer player data").getOrCreate()

players = spark_session.read.format("csv").option("header", "true").load(
    r'C:\Users\achakala.sreenath\PycharmProjects\spark2\demo\datasets\player.csv')

player_attributes = spark_session.read.format("csv").option("header", "true").load(
    r'C:\Users\achakala.sreenath\PycharmProjects\spark2\demo\datasets\player_attributes.csv')
player_attributes = player_attributes.drop("player_fifa_api_id","id")
players_and_attributes = player_attributes.join(broadcast(players),["player_api_id"],"left")

players_and_attributes.write.partitionBy("player_api_id").option("header","true").parquet("partiotioned.parquet")