from pyspark.accumulators import AccumulatorParam
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, broadcast

spark_session = SparkSession.builder.appName("analysing soccer player data").getOrCreate()

players = spark_session.read.format("csv").option("header", "true").load(
    r'C:\Users\achakala.sreenath\PycharmProjects\spark2\demo\datasets\player.csv')

player_attributes = spark_session.read.format("csv").option("header", "true").load(
    r'C:\Users\achakala.sreenath\PycharmProjects\spark2\demo\datasets\player_attributes.csv')

player_heading_accuracy = player_attributes.select("player_api_id", "heading_accuracy").join(broadcast(players),
                                                                                             ["player_api_id"], "inner")

short_height_count = spark_session.sparkContext.accumulator(0)
medium_short_height_count = spark_session.sparkContext.accumulator(0)
medium_high_height_count = spark_session.sparkContext.accumulator(0)
tall_height_count = spark_session.sparkContext.accumulator(0)

short_height_count_with_heading_accuracy = spark_session.sparkContext.accumulator(0)
medium_short_height_count_with_heading_accuracy = spark_session.sparkContext.accumulator(0)
medium_high_height_count_with_heading_accuracy = spark_session.sparkContext.accumulator(0)
tall_height_count_with_heading_accuracy = spark_session.sparkContext.accumulator(0)


class CustomAccumulator(AccumulatorParam):
    def zero(self, v1):
        return [0.0] * len(v1)

    def addInPlace(self, v1, v2):
        for i in range(len(v1)):
            v1[i] += v2[i]
        return v1

def height_count(row):
    height = float(row.height)
    if height <= 175:
        short_height_count_with_heading_accuracy.add(1)
    elif 175 < height <= 183:
        medium_short_height_count_with_heading_accuracy.add(1)
    elif 183 < height <= 190:
        medium_high_height_count_with_heading_accuracy.add(1)
    elif height > 190:
        tall_height_count_with_heading_accuracy.add(1)


def height_count_with_heading_accuracy(row, threshold):
    height = float(row.height)
    if row.heading_accuracy is not None:
        heading_accuracy = float(row.heading_accuracy)
        if heading_accuracy < threshold:
            return

    if height <= 175:
        short_height_count.add(1)
    elif 175 < height <= 183:
        medium_short_height_count.add(1)
    elif 183 < height <= 190:
        medium_high_height_count.add(1)
    elif height > 190:
        tall_height_count.add(1)


def extract_year(player_attributes):
    year_extract_udf = udf(lambda x: x.split('-')[0])
    player_attributes = player_attributes.withColumn("year", year_extract_udf(player_attributes.date))
    # player_attributes.show(5)
    player_attributes = player_attributes.drop("date")
    return player_attributes


if __name__ == "__main__":
    player_attributes = extract_year(player_attributes)
    player_attributes = player_attributes.drop("player_fifa_api_id")
    player_attributes = player_attributes.filter(player_attributes.year == '2016')
    player_attributes = player_attributes.select("player_api_id", "finishing", "acceleration", "shot_power")
    player_attributes.select("shot_power").show(5)
    player_attributes = player_attributes.groupBy("player_api_id").agg({"finishing": "avg",
                                                                        "shot_power": "avg",
                                                                        "acceleration": "avg",
                                                                        })
    player_attributes = player_attributes.withColumnRenamed("avg(finishing)", "finishing_avg")
    player_attributes = player_attributes.withColumnRenamed("avg(acceleration)", "acceleration_avg")
    player_attributes = player_attributes.withColumnRenamed("avg(shot_power)", "shot_power_avg")
    weight_finishing = 1
    weight_acceleration = 2
    weight_shot_power = 1
    total_weight = weight_acceleration + weight_finishing + weight_shot_power
    player_attributes = player_attributes.withColumn('strike_grade',
                                                     (
                                                             (weight_shot_power * player_attributes["shot_power_avg"]) +
                                                             (weight_finishing * player_attributes["finishing_avg"]) +
                                                             (weight_acceleration * player_attributes[
                                                                 "acceleration_avg"])
                                                     ) / total_weight
                                                     )
    player_attributes = player_attributes.drop('finishing_avg', 'acceleration_avg', 'shot_power_avg')
    strikers = player_attributes.filter(player_attributes.strike_grade >= 70).orderBy(
        player_attributes.strike_grade.desc())
    # player_striking_grades = player_attributes.join(players,player_attributes.player_api_id == players.player_api_id)
    # to perform the join operation, a copy of players dataframe will be used in all the nodes in the cluster which is an expensive operation
    # to avoid this we can broadcast(i.e.. single read-only copy)  the smaller dataframe across all the tasks in a worker
    #strikers = player_attributes.join(players, ["player_api_id"])
    striker_details = players.select("player_api_id", "player_name").join(broadcast(strikers), ["player_api_id"],
                                                                          "inner")

    # analysis of heading accuracy and height
    player_heading_accuracy.foreach(lambda x: height_count(x))
    player_heading_accuracy.foreach(lambda x: height_count_with_heading_accuracy(row=x, threshold=70.0))
    percentage_heading_accuracy = (short_height_count.value / short_height_count_with_heading_accuracy.value * 100,
                                   medium_short_height_count.value / medium_short_height_count_with_heading_accuracy.value * 100,
                                   medium_high_height_count.value / medium_high_height_count_with_heading_accuracy.value * 100,
                                   tall_height_count.value / tall_height_count_with_heading_accuracy.value * 100)
    #print(spark_session.sparkContext.accumulator([1,2,34],CustomAccumulator()))