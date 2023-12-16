from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PySparkTest").getOrCreate()

spark.range(10).show()

spark.stop()