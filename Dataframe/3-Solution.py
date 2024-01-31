
##import from 1-how to create Dataframe

#1Display first 3 rows 
df.show(3)

##2 Show the summary statistics (count, mean, stddev, min, and max) for the 'age' column
df.describe("age").show()


##3 .Filter and display only the rows where the age is greater than 25. 
df.filter(col("age")>'25').show()  or df.filter(df.age>25).show()

##4 Group the data by 'city' and show the average age for each city.
df.groupBy('city').agg(avg("age").alias('avg_age')).show()

