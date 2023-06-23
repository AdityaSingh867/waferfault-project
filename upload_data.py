from pymongo.mongo_client import MongoClient
import pandas as pd
import json

## Uniform resource indentifier
uri = "mongodb+srv://Adityasingh:Adityasingh@cluster0.98n26pg.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

## Creat database name and Collection name

DATABASE_NAME = "pwskills"
COLLECTION__NAME = "Waferfault"

## Read data as a DataFrame

df = pd.read_csv(r"D:\name_1\name_1\sensor_fault\notebooks\wafer_23012020_041211.csv")
df.drop('Unnamed: 0' , axis=1 , inplace=True)
# Convert into json

json_records = list(json.loads(df.T.to_json()).values())

## Now dump the data into Database

client[DATABASE_NAME][COLLECTION__NAME].insert_many(json_records)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)