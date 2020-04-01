# Databricks notebook source
# MAGIC %sql
# MAGIC --SHOW TABLES
# MAGIC --SHOW DATABASES
# MAGIC --CREATE table test1 AS SELECT 1, "one"
# MAGIC CREATE TABLE test.tbl1 USING PARQUET LOCATION '/myfolder/tables/tbl1'

# COMMAND ----------

from pyspark.sql.types import IntegerType, StringType
#dbutils.fs.mkdirs("/myfolder/tables")
#spark.createDataFrame([(1, "one")], ["id", "data"]).write.format("parquet").save("/myfolder/tables/tbl1")
#spark.createDataFrame([(1, "one")], ["id", "data"]).write.format("parquet").save("/myfolder/tables/tbl2")
spark.createDataFrame([(1, "one")], ["id", "data"]).write.format("csv").save("/myfolder/tables/tbl3")

# COMMAND ----------

