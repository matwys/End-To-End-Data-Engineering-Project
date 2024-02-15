# Databricks notebook source
table_name = []

for i in dbutils.fs.ls('mnt/silver/SalesLT/'):
    table_name.append(i.name.split('/')[0])

# COMMAND ----------

for name in table_name:
    path = '/mnt/silver/SalesLT/' + name
    print(path)
    df = spark.read.format('delta').load(path)

    column_names = df.columns

    for old_col_name in column_names:
        #Convert column name format from ColumnName to Column_Name format
        new_col_name = "".join(["_" + char if char.isupper() and not old_col_name[i-1].isupper() else char for i, char in enumerate(old_col_name)]).lstrip("_")
        df = df.withColumnRenamed(old_col_name, new_col_name)

    output_path = '/mnt/gold/SalesLT/' + name + '/'
    df.write.format('delta').mode("overwrite").save(output_path)


