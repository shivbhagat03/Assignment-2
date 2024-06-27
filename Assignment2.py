# %%
import subprocess
import sys
import pkg_resources

def install_influxdb_client():
    try:
        pkg_resources.get_distribution('influxdb-client')
        print("influxdb-client is already installed")
    except pkg_resources.DistributionNotFound:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "influxdb-client"])

install_influxdb_client()

# %%
INFLUXDB_TOKEN="UHRg4yKQlH6LyVzBQpWEK7ynjAoP1iFBCz0pKDh8ZmosJj_EQIBgGx-gd_IZLuMpZ3_t-NtjZJIrM1to3nzOxg=="



# %%
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "test"
url = "http://localhost:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)


# %%
import time
from influxdb_client import InfluxDBClient, Point, WriteOptions

# Configuration details
bucket = "iris"
org = "test"
token = "UHRg4yKQlH6LyVzBQpWEK7ynjAoP1iFBCz0pKDh8ZmosJj_EQIBgGx-gd_IZLuMpZ3_t-NtjZJIrM1to3nzOxg=="
url = "http://localhost:8086"  # Adjust the URL as per your InfluxDB setup

# Initialize the client
client = InfluxDBClient(url=url, token=token, org=org)

# Get the write API
write_api = client.write_api(write_options=WriteOptions(batch_size=1))

for value in range(5):
    point = (
        Point("measurement1")
        .tag("tagname1", "tagvalue1")
        .field("field1", value)
    )
    write_api.write(bucket=bucket, org=org, record=point)
    time.sleep(1)  # separate points by 1 second

# Close the client
client.close()



# %%
from influxdb_client import InfluxDBClient

# Configuration details
bucket = "iris"
org = "test"
token = "UHRg4yKQlH6LyVzBQpWEK7ynjAoP1iFBCz0pKDh8ZmosJj_EQIBgGx-gd_IZLuMpZ3_t-NtjZJIrM1to3nzOxg=="  # Replace with your actual token
url = "http://localhost:8086"  # Adjust the URL as per your InfluxDB setup

# Initialize the client
client = InfluxDBClient(url=url, token=token, org=org)

# Get the query API
query_api = client.query_api()

# Define the query
query = """
from(bucket: "iris")
  |> range(start: -10m)
  |> filter(fn: (r) => r._measurement == "measurement1")
"""

# Execute the query
tables = query_api.query(query, org="test")

# Iterate over the query results and print records
for table in tables:
    for record in table.records:
        print(record)

# Close the client
client.close()


# %%
from influxdb_client import InfluxDBClient

# Configuration details
bucket = "iris"
org = "test"
token = "UHRg4yKQlH6LyVzBQpWEK7ynjAoP1iFBCz0pKDh8ZmosJj_EQIBgGx-gd_IZLuMpZ3_t-NtjZJIrM1to3nzOxg=="  # Replace with your actual token
url = "http://localhost:8086"  # Adjust the URL as per your InfluxDB setup

# Initialize the client
client = InfluxDBClient(url=url, token=token, org=org)


query_api = client.query_api()

query = """from(bucket: "iris")
  |> range(start: -10m)
  |> filter(fn: (r) => r._measurement == "measurement1")
  |> mean()"""
tables = query_api.query(query, org="test")

for table in tables:
    for record in table.records:
        print(record)

client.close()



