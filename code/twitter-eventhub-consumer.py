# Databricks notebook source
# MAGIC %md # Install EventHub

# COMMAND ----------

# MAGIC %pip install azure-eventhub

# COMMAND ----------

# MAGIC %md # Create EventHubConsumer

# COMMAND ----------

from azure.eventhub import EventData, EventHubConsumerClient,EventHubSharedKeyCredential
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import *
import json

eventhub_policy = dbutils.secrets.get(scope = "TwitterStreamKV", key = "EventHubPolicy")
eventhub_servicebus = dbutils.secrets.get(scope = "TwitterStreamKV", key = "EventHubServicebus")
eventhub_name = dbutils.secrets.get(scope = "TwitterStreamKV", key = "EventHubName")
eventhub_namespace = dbutils.secrets.get(scope = "TwitterStreamKV", key = "EventHubNamespace")
eventhub_sas = dbutils.secrets.get(scope="TwitterStreamKV", key = "EventHubSAS")

sk = EventHubSharedKeyCredential(eventhub_policy,eventhub_sas)
ehcc = EventHubConsumerClient(fully_qualified_namespace=eventhub_servicebus, credential=sk,eventhub_name=eventhub_name, consumer_group='$Default')

# COMMAND ----------

# MAGIC %md # Define Delta Table

# COMMAND ----------

# MAGIC %sql CREATE TABLE IF NOT EXISTS default.tweets (author_id STRING,created_at DATE,text STRING,user_name STRING, name STRING) USING DELTA

# COMMAND ----------

# MAGIC %md # EventHub to Delta

# COMMAND ----------

import datetime
from dateutil.parser import parse
import re
def receive_event(partition, event):
  jtweet = json.loads(event.body_as_str(encoding='UTF-8'))
  author_id = jtweet["data"]["author_id"]
  created_at = parse(jtweet["data"]["created_at"])
  created_at = created_at.strftime("%Y-%m-%d")
  text = jtweet["data"]["text"]
  user_name = jtweet["includes"]["users"][0]["username"]
  name = jtweet["includes"]["users"][0]["name"]

  
ehcc.receive(receive_event)
