import redis
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
conf = (SparkConf().setMaster("local").setAppName("SparkApp").set("spark.executor.memory", "1g"))
sc = SparkContext(conf = conf)
sc.setLogLevel("OFF")
sqlContext=SQLContext(sc)
prodDf=sqlContext.read.json("ProductData.json")
prodDf.show()
prodDf.select("Brand").show();
col=raw_input("Enter Color :");
prodDf.filter(prodDf["Color"]==col).show()
prodDf.limit(3).show();
date=raw_input("Enter Date :");
prodDf.filter(prodDf["DateAdded"]==date).groupBy("Brand").count().show()
