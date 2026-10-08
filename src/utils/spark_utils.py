from pyspark.sql import SparkSession
from pyspark.sql.types import *
import os
from dotenv import load_dotenv

load_dotenv()

def create_spark_session(app_name="vessel-intelligence"):
    """
    Create and configure Spark session
    """
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .config("spark.driver.memory", "8g") \
        .config("spark.executor.memory", "8g") \
        .config("spark.sql.shuffle.partitions", "200") \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.databricks.delta.optimizeWrite.enabled", "true") \
        .config("spark.databricks.delta.autoCompact.enabled", "true") \
        .getOrCreate()
    
    return spark

def get_config(key):
    """
    Get configuration value from environment
    """
    return os.getenv(key)

def log_message(message, level="INFO"):
    """
    Log message with timestamp
    """
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")