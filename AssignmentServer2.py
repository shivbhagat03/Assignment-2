# %%
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install influxdb-client
install("influxdb-client")


# %%
INFLUXDB_TOKEN="y2QE5G5dztY5RPdM8DJt7K1s2Vn5aGuvKf2OT-6PDCvp0RyEJg0YrCslHo-1QkYLTptHudnLBBGCHvNJq_0ntw=="

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
token = "y2QE5G5dztY5RPdM8DJt7K1s2Vn5aGuvKf2OT-6PDCvp0RyEJg0YrCslHo-1QkYLTptHudnLBBGCHvNJq_0ntw=="
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
token = "y2QE5G5dztY5RPdM8DJt7K1s2Vn5aGuvKf2OT-6PDCvp0RyEJg0YrCslHo-1QkYLTptHudnLBBGCHvNJq_0ntw=="  # Replace with your actual token
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
token = "y2QE5G5dztY5RPdM8DJt7K1s2Vn5aGuvKf2OT-6PDCvp0RyEJg0YrCslHo-1QkYLTptHudnLBBGCHvNJq_0ntw=="  # Replace with your actual token
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


# %%
# Install Flask
subprocess.check_call(['pip3', 'install', 'Flask'])


# %%
import sys

def install_packages():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Flask", "requests"])

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
#flask_thread.shutdown()


# %%
packages = ["Flask", "influxdb-client"]

# Install each package
for package in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# %%
def install_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# Install pandas
install_package("pandas")

# %%
from flask import Flask, jsonify
from werkzeug.serving import make_server
import threading
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB setup
url = "http://localhost:8086"  # InfluxDB URL
bucket = "iris"
org = "test"
token = "y2QE5G5dztY5RPdM8DJt7K1s2Vn5aGuvKf2OT-6PDCvp0RyEJg0YrCslHo-1QkYLTptHudnLBBGCHvNJq_0ntw=="

# Create an InfluxDB client
client = InfluxDBClient(url=url, token=token, org=org)

# Initialize Flask app
app = Flask(__name__)

# Flask endpoint to fetch data from InfluxDB
@app.route("/fetch_data")
def fetch_data():
    try:
        # InfluxDB query to fetch data
        query = f'from(bucket: "{bucket}") |> range(start: -1h) |> filter(fn: (r) => r._measurement == "your_measurement")'
        result = client.query_api().query(org=org, query=query)
        
        # Process the result and convert to JSON format
        data = []
        for table in result:
            for record in table.records:
                data.append({
                    "time": record.get_time(),
                    "value": record.get_value()
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

# Test the /fetch_data endpoint
import requests
try:
    response = requests.get("http://127.0.0.1:5000/fetch_data")
    if response.status_code == 200:
        print("API is running. GET /fetch_data response:", response.json())
    else:
        print("API is not running. Received status code:", response.status_code)
except requests.ConnectionError:
    print("API is not running. Failed to connect.")

# Stop the Flask server when done testing
#flask_thread.shutdown()


# %%



