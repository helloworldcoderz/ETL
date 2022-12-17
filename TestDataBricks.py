# Databricks notebook source
print("hello")

# COMMAND ----------

# MAGIC %md
# MAGIC This is a sample workbook to read and write data from CSV to table

# COMMAND ----------

dbutils.fs.unmount("/mnt/dbsmount/raw")
dbutils.fs.unmount("/mnt/dbsmount/processed")

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "bd6eca9a-bdbd-4f59-bbf4-b57801cb6125",
          "fs.azure.account.oauth2.client.secret": "ACR8Q~sdx5aEg_M.Awl_GeqpJduxeVelvnC69akQ",
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/e10b6b02-6085-4912-9810-31f6fc637e88/oauth2/token"}

dbutils.fs.mount(
  source = "abfss://raw@azuredatabricksstgacc.dfs.core.windows.net/",
  mount_point = "/mnt/dbsmount/raw",
  extra_configs = configs)


dbutils.fs.mount(
  source = "abfss://processed@azuredatabricksstgacc.dfs.core.windows.net/",
  mount_point = "/mnt/dbsmount/processed",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.list()
