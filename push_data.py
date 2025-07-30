import os
import sys
import json
import certifi
import pandas as pd
import pymongo

from dotenv import load_dotenv
from networksecurity.exception.exception import NetworksecurityError
from networksecurity.logging.logger import logger

# ✅ Load environment variables
load_dotenv()
MONGODB_URL = os.getenv('MONGO_DB_URL')
print("MongoDB URL:", MONGODB_URL)

# ✅ Certificate for secure MongoDB connection
ca = certifi.where()

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworksecurityError(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            # 🔍 Check if file exists
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"File not found at path: {file_path}")
            
            # 📥 Read CSV and convert to JSON records
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworksecurityError(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            # 🛡 Connect to MongoDB
            mongo_client = pymongo.MongoClient(MONGODB_URL, tlsCAFile=ca)
            db = mongo_client[database]
            coll = db[collection]

            # ⬆ Insert all records
            result = coll.insert_many(records)
            return len(result.inserted_ids)
        except Exception as e:
            raise NetworksecurityError(e, sys)

if __name__ == '__main__':
    try:
        # ✅ Use FULL path of the CSV file (change this to match your exact path)
        FILE_PATH = r"Netwrork_Data\phisingData.csv"
        DATABASE = "Anurag"
        COLLECTION = "NetworkData"

        # 🚀 Create object
        networkobj = NetworkDataExtract()

        # 📤 Convert CSV to JSON
        records = networkobj.csv_to_json_convertor(FILE_PATH)
        print(f"✅ Records Converted: {len(records)}")

        # 📥 Insert into MongoDB
        no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
        print(f"✅ Records Inserted into MongoDB: {no_of_records}")

    except Exception as e:
        print("❌ Error:", e)
