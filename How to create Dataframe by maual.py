from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Create a Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Define the schema for the data
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("city", StringType(), True),
])

# Create a DataFrame
data = [("Alice", 25, "New York"),
        ("Bob", 30, "San Francisco"),
        ("Charlie", 22, "Los Angeles"),
        ("David", 35, "Chicago")]

df = spark.createDataFrame(data, schema=schema)

# Show the DataFrame
df.show()
