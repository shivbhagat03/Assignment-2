# %%
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install influxdb-client package
install('influxdb-client')


# %%
INFLUXDB_TOKEN="vgJslcjFdiqPRz9q3e6h2Q16AYHmjwHMGVEhFs2oojY3oZLDddavvI2jXC2wofQ8-dDioO-_L5RwnCR8yvSnMQ=="

# %%
import os

# Command to install influxdb package
os.system('pip3 install influxdb')



# %%
import csv

csv_file_path = r'C:\Users\Dell\Downloads\internship(JBM)\energydata_complete.csv'

def read_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

data = read_data(csv_file_path)

# Print the first few rows to inspect the date format
for i, row in enumerate(data[:5]):  # Adjust the number to print more rows if needed
    print(f"Row {i + 1}: {row}")


# %%
import csv
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision, WriteOptions

# Parameters for InfluxDB
token = "vgJslcjFdiqPRz9q3e6h2Q16AYHmjwHMGVEhFs2oojY3oZLDddavvI2jXC2wofQ8-dDioO-_L5RwnCR8yvSnMQ=="
org = "test"
bucket = "bucket1"
url = "http://localhost:8086"

# Function to read data from CSV file
def read_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

# Path to the CSV file
csv_file_path = r'C:\Users\Dell\Downloads\internship(JBM)\energydata_complete.csv'

# Read the data
data = read_data(csv_file_path)

# Print the first few rows to inspect the date format
for i, row in enumerate(data[:1935]):  # Adjust the number to print more rows if needed
    print(f"Row {i + 1}: {row}")

# Initialize InfluxDB client
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=WriteOptions(write_type="synchronous"))

# Function to convert date to ISO format
def convert_date_to_iso(date_str):
    dt = datetime.strptime(date_str, '%m/%d/%Y %H:%M')
    return dt.isoformat() + 'Z'

# Write data to InfluxDB
for row in data:
    iso_date = convert_date_to_iso(row["date"])
    point = Point("energy_data") \
        .field("Appliances", float(row["Appliances"])) \
        .field("lights", float(row["lights"])) \
        .field("T1", float(row["T1"])) \
        .field("RH_1", float(row["RH_1"])) \
        .field("T2", float(row["T2"])) \
        .field("RH_2", float(row["RH_2"])) \
        .field("T3", float(row["T3"])) \
        .field("RH_3", float(row["RH_3"])) \
        .field("T4", float(row["T4"])) \
        .field("RH_4", float(row["RH_4"])) \
        .field("T5", float(row["T5"])) \
        .field("RH_5", float(row["RH_5"])) \
        .field("T6", float(row["T6"])) \
        .field("RH_6", float(row["RH_6"])) \
        .field("T7", float(row["T7"])) \
        .field("RH_7", float(row["RH_7"])) \
        .field("T8", float(row["T8"])) \
        .field("RH_8", float(row["RH_8"])) \
        .field("T9", float(row["T9"])) \
        .field("RH_9", float(row["RH_9"])) \
        .field("T_out", float(row["T_out"])) \
        .field("Press_mm_hg", float(row["Press_mm_hg"])) \
        .field("RH_out", float(row["RH_out"])) \
        .field("Windspeed", float(row["Windspeed"])) \
        .field("Visibility", float(row["Visibility"])) \
        .field("Tdewpoint", float(row["Tdewpoint"])) \
        .field("rv1", float(row["rv1"])) \
        .field("rv2", float(row["rv2"])) \
        .time(iso_date, WritePrecision.NS)
    
    # Write point to InfluxDB
    write_api.write(bucket=bucket, org=org, record=point)

print("Data has been written to InfluxDB.")


# %%
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "test"
url = "http://localhost:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)


# %%
import pandas as pd
from influxdb_client import InfluxDBClient, Point, WriteOptions
from datetime import datetime

# Configuration details
bucket = "bucket1"
org = "test"
token = "vgJslcjFdiqPRz9q3e6h2Q16AYHmjwHMGVEhFs2oojY3oZLDddavvI2jXC2wofQ8-dDioO-_L5RwnCR8yvSnMQ=="
url = "http://localhost:8086"  # Adjust the URL as per your InfluxDB setup

# Load the CSV file
file_path =r'C:\Users\Dell\Downloads\internship(JBM)\energydata_complete.csv'
data = pd.read_csv(file_path)

# Function to convert date string to datetime object
def parse_date(date_str):
    return datetime.strptime(date_str, '%m/%d/%Y %H:%M')

# Initialize the client
client = InfluxDBClient(url=url, token=token, org=org)

# Get the write API
write_api = client.write_api(write_options=WriteOptions(write_type="synchronous"))

# Write data points to InfluxDB
for index, row in data.iterrows():
    point = (
        Point("measurement1")
        .tag("source", "sensor")
        .field("Appliances", row["Appliances"])
        .field("lights", row["lights"])
        .field("T1", row["T1"])
        .field("RH_1", row["RH_1"])
        .field("T2", row["T2"])
        .field("RH_2", row["RH_2"])
        .time(parse_date(row["date"]))  # Convert the date to datetime object
    )
    write_api.write(bucket=bucket, org=org, record=point)

    # Print some of the data being written for verification
    if index < 5:  # Print the first 5 rows for verification
        print(point)

# Close the client
client.close()


# %%
from influxdb_client import InfluxDBClient

# Configuration details
bucket = "bucket1"
org = "test"
token = "vgJslcjFdiqPRz9q3e6h2Q16AYHmjwHMGVEhFs2oojY3oZLDddavvI2jXC2wofQ8-dDioO-_L5RwnCR8yvSnMQ=="
url = "http://localhost:8086"  # Adjust the URL as per your InfluxDB setup

# Initialize the client
client = InfluxDBClient(url=url, token=token, org=org)

# Get the query API
query_api = client.query_api()

# Define the query
query = f"""
from(bucket: "{bucket}")
  |> range(start: 2016-01-11T17:00:00Z, stop: 2016-01-11T18:20:00Z)  // Adjust the date range to your dataset
  |> filter(fn: (r) => r._measurement == "measurement1")
  |> filter(fn: (r) => r._field == "Appliances" or r._field == "lights" or r._field == "T1" or r._field == "RH_1" or r._field == "T2" or r._field == "RH_2")
"""

# Execute the query
tables = query_api.query(query=query, org=org)

# Iterate over the query results and print records
for table in tables:
    for record in table.records:
        print(f"Time: {record.get_time()}, Measurement: {record.get_measurement()}, Field: {record.get_field()}, Value: {record.get_value()}")

# Close the client
client.close()


# %%
from influxdb_client import InfluxDBClient

# Configuration details
bucket = "bucket1"
org = "test"
token = "vgJslcjFdiqPRz9q3e6h2Q16AYHmjwHMGVEhFs2oojY3oZLDddavvI2jXC2wofQ8-dDioO-_L5RwnCR8yvSnMQ=="
url = "http://localhost:8086"  # Adjust the URL as per your InfluxDB setup

# Initialize the client
client = InfluxDBClient(url=url, token=token, org=org)

# Get the query API
query_api = client.query_api()

# Define the query
query = f"""
from(bucket: "{bucket}")
  |> range(start: 2016-01-11T17:00:00Z, stop: 2016-01-11T18:20:00Z)
  |> filter(fn: (r) => r._measurement == "measurement1")
  |> filter(fn: (r) => r._field == "Appliances" or r._field == "lights" or r._field == "T1" or r._field == "RH_1" or r._field == "T2" or r._field == "RH_2")
  |> mean()
"""

# Execute the query
tables = query_api.query(query=query, org=org)

# Iterate over the query results and print records
for table in tables:
    for record in table.records:
        print(record.values)  # Print the entire record dictionary to inspect keys

# Close the client
client.close()


# %%
'''import time
from influxdb_client import InfluxDBClient, Point, WriteOptions

# Configuration details
bucket = "bucket1"
org = "test"
token = "vgJslcjFdiqPRz9q3e6h2Q16AYHmjwHMGVEhFs2oojY3oZLDddavvI2jXC2wofQ8-dDioO-_L5RwnCR8yvSnMQ=="
url = "http://localhost:8086"  # Adjust the URL as per your InfluxDB setup

# Initialize the client
client = InfluxDBClient(url=url, token=token, org=org)

# Get the write API
write_api = client.write_api(write_options=WriteOptions(write_type="synchronous"))

for value in range(5):
    point = (
        Point("measurement1")
        .tag("tagname1", "tagvalue1")
        .field("field1", value)
    )
    write_api.write(bucket=bucket, org=org, record=point)
    time.sleep(1)  # separate points by 1 second

# Close the client
client.close()'''


# %%
'''from influxdb_client import InfluxDBClient

# Configuration details
bucket = "bucket1"
org = "test"
token = "vgJslcjFdiqPRz9q3e6h2Q16AYHmjwHMGVEhFs2oojY3oZLDddavvI2jXC2wofQ8-dDioO-_L5RwnCR8yvSnMQ=="  # Replace with your actual token
url = "http://localhost:8086"  # Adjust the URL as per your InfluxDB setup

# Initialize the client
client = InfluxDBClient(url=url, token=token, org=org)

# Get the query API
query_api = client.query_api()

# Define the query
query = f"""
from(bucket: "{bucket}")
  |> range(start: -24h)
  |> filter(fn: (r) => r._measurement == "energy_data")
"""

# Execute the query
tables = query_api.query(query=query, org=org)

# Iterate over the query results and print records
for table in tables:
    for record in table.records:
        print(f"Time: {record.get_time()}, Measurement: {record.get_measurement()}, Field: {record.get_field()}, Value: {record.get_value()}")

# Close the client
client.close()'''


# %%
'''from influxdb_client import InfluxDBClient

# Configuration details
bucket = "bucket1"
org = "test"
token = "vgJslcjFdiqPRz9q3e6h2Q16AYHmjwHMGVEhFs2oojY3oZLDddavvI2jXC2wofQ8-dDioO-_L5RwnCR8yvSnMQ=="  # Replace with your actual token
url = "http://localhost:8086"  # Adjust the URL as per your InfluxDB setup

# Initialize the client
client = InfluxDBClient(url=url, token=token, org=org)


query_api = client.query_api()

query = """from(bucket: "bucket1")
  |> range(start: -10m)
  |> filter(fn: (r) => r._measurement == "measurement1")
  |> mean()"""
tables = query_api.query(query, org="test")

for table in tables:
    for record in table.records:
        print(record)

client.close()'''


# %%
import os

os.system('pip3 install Flask')


# %%
# setup_environment.py
import os

def install_packages():
    os.system("pip3 install Flask requests")

if __name__ == "__main__":
    install_packages()



# %%
import threading
from flask import Flask, request, jsonify
from werkzeug.serving import make_server

app = Flask(__name__)

@app.route("/hello_world")
def home():
    return "Hello, World!"

@app.route("/data", methods=["POST"])
def data():
    content = request.json
    return jsonify(content)

class FlaskThread(threading.Thread):
    def __init__(self, app):
        threading.Thread.__init__(self)
        self.srv = make_server('127.0.0.1', 5000, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        print("Starting server")
        self.srv.serve_forever()

    def shutdown(self):
        print("Shutting down server")
        self.srv.shutdown()

flask_thread = FlaskThread(app)
flask_thread.start()

# Step 2: Test the API
import requests
import time

# Wait a bit for the server to start
time.sleep(2)

# Test the GET /hello_world endpoint
try:
    response = requests.get("http://127.0.0.1:5000/hello_world")
    if response.status_code == 200:
        print("API is running. GET /hello_world response:", response.text)
    else:
        print("API is not running. Received status code:", response.status_code)
except requests.ConnectionError:
    print("API is not running. Failed to connect.")

# Test the POST /data endpoint
try:
    response = requests.post("http://127.0.0.1:5000/data", json={"key": "value"})
    if response.status_code == 200:
        print("POST /data response:", response.json())
    else:
        print("Failed to POST to /data. Received status code:", response.status_code)
except requests.ConnectionError:
    print("Failed to connect to /data.")

# Step 3: Stop the Flask server
flask_thread.shutdown()


# %%
# setup_environment.py
import os

def install_packages():
    os.system("pip3 install Flask influxdb-client")

if __name__ == "__main__":
    install_packages()



# %%
# setup_environment.py
import os

def install_packages():
    os.system("pip3 install pandas")

if __name__ == "__main__":
    install_packages()


# %%
from flask import Flask, jsonify
from influxdb_client import InfluxDBClient
from werkzeug.serving import make_server
import threading
import traceback

# InfluxDB setup
url = "http://localhost:8086"  # InfluxDB URL
bucket = "bucket1"
org = "test"
token = "vgJslcjFdiqPRz9q3e6h2Q16AYHmjwHMGVEhFs2oojY3oZLDddavvI2jXC2wofQ8-dDioO-_L5RwnCR8yvSnMQ=="

# Create an InfluxDB client
client = InfluxDBClient(url=url, token=token, org=org)

# Initialize Flask app
app = Flask(__name__)

# Flask endpoint to fetch data from InfluxDB
@app.route("/fetch_data")
def fetch_data():
    try:
        # InfluxDB query to fetch data
        query =  f"""
        from(bucket: "{bucket}")
        |> range(start: -1y)
        |> filter(fn: (r) => r._measurement == "energy_data")
        |> filter(fn: (r) => r._field == "Appliances" or r._field == "lights" or r._field == "T1" or r._field == "RH_1" or r._field == "T2" or r._field == "RH_2" or
                             r._field == "T3" or r._field == "RH_3" or r._field == "T4" or r._field == "RH_4" or r._field == "T5" or r._field == "RH_5" or
                             r._field == "T6" or r._field == "RH_6" or r._field == "T7" or r._field == "RH_7" or r._field == "T8" or r._field == "RH_8" or
                             r._field == "T9" or r._field == "RH_9" or r._field == "T_out" or r._field == "Press_mm_hg" or r._field == "RH_out" or 
                             r._field == "Windspeed" or r._field == "Visibility" or r._field == "Tdewpoint" or r._field == "rv1" or r._field == "rv2")
        """
        result = client.query_api().query(org=org, query=query)
        
        # Process the result and convert to JSON format
        data = []
        for table in result:
            for record in table.records:
                data.append({
                    "time": record.get_time().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    "measurement": record.get_measurement(),
                    "field": record.get_field(),
                    "value": record.get_value()
                })
        
        # Debug: Print the data
        print("Fetched data:", data)
        
        return jsonify(data)
    except Exception as e:
        print(f"Error: {e}")
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

# FlaskThread class to run the server in a separate thread
class FlaskThread(threading.Thread):
    def __init__(self, app):
        threading.Thread.__init__(self)
        self.srv = make_server('127.0.0.1', 5000, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        print("Starting server")
        self.srv.serve_forever()

    def shutdown(self):
        print("Shutting down server")
        self.srv.shutdown()

# Start the Flask server in a new thread
flask_thread = FlaskThread(app)
flask_thread.start()

# Wait a bit for the server to start (optional)
import time
time.sleep(2)  # Adjust as needed

# Test the /fetch_data endpoint
import requests
try:
    response = requests.get("http://127.0.0.1:5000/fetch_data")
    if response.status_code == 200:
        print("API is running. GET /fetch_data response:", response.json())
    else:
        print("API is not running. Received status code:", response.status_code)
        print("Response content:", response.json())
except requests.ConnectionError:
    print("API is not running. Failed to connect.")

# Stop the Flask server when done testing
# flask_thread.shutdown()


# %%
from flask import Flask, jsonify
from werkzeug.serving import make_server
import threading
from influxdb_client import InfluxDBClient

# InfluxDB setup
url = "http://localhost:8086"  # InfluxDB URL
bucket = "bucket1"
org = "test"
token = "vgJslcjFdiqPRz9q3e6h2Q16AYHmjwHMGVEhFs2oojY3oZLDddavvI2jXC2wofQ8-dDioO-_L5RwnCR8yvSnMQ=="

# Create an InfluxDB client
client = InfluxDBClient(url=url, token=token, org=org)

# Initialize Flask app
app = Flask(__name__)

# Flask endpoint to retrieve data from InfluxDB
@app.route("/retrieve_data")
def retrieve_data():
    print("Inside /retrieve_data endpoint")  # Debug log
    try:
        # InfluxDB query to fetch data
        query = (
            f'from(bucket: "{bucket}") '
            '|> range(start: -30d) '  # Adjust the time range as needed
            '|> filter(fn: (r) => r["_measurement"] == "appliances") '
            '|> limit(n: 5)'  # Retrieve only a limited number of rows for sampling
        )
        result = client.query_api().query(org=org, query=query)
        
        # Process the result and convert to JSON format
        data = []
        for table in result:
            for record in table.records:
                data.append({
                    "time": record.get_time().isoformat(),
                    "measurement": record.get_measurement(),
                    "field": record.get_field(),
                    "value": record.get_value(),
                    "tags": record.values.get("_tags", {})
                })
        
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# FlaskThread class to run the server in a separate thread
class FlaskThread(threading.Thread):
    def __init__(self, app):
        threading.Thread.__init__(self)
        self.srv = make_server('127.0.0.1', 5000, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        print("Starting server")
        self.srv.serve_forever()

    def shutdown(self):
        print("Shutting down server")
        self.srv.shutdown()

# Start the Flask server in a new thread
flask_thread = FlaskThread(app)
flask_thread.start()

# Wait a bit for the server to start (optional)
import time
time.sleep(2)  # Adjust as needed

# Test the /retrieve_data endpoint
import requests
try:
    response = requests.get("http://127.0.0.1:5000/retrieve_data")
    if response.status_code == 200:
        print("API is running. GET /retrieve_data response:", response.json())
    else:
        print("API is not running. Received status code:", response.status_code)
except requests.ConnectionError:
    print("API is not running. Failed to connect.")

# Stop the Flask server when done testing
# flask_thread.shutdown()



