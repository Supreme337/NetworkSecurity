import os
import pandas as pd
import pymongo
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
DATABASE_NAME = "Harsh"              
COLLECTION_NAME = "NetworkSecurity"   
CSV_FILE_PATH = r"C:\NetworkSecurity\Network_Data\phisingData.csv"  

def insert_csv_to_mongodb(csv_path, db_name, collection_name):
    try:
        # 2. Connect to MongoDB
        client = pymongo.MongoClient(MONGO_DB_URL)
        db = client[db_name]
        collection = db[collection_name]

        # 3. Read CSV into DataFrame
        df = pd.read_csv(csv_path)
        print(f"✅ Loaded CSV successfully with shape: {df.shape}")

        # 4. Convert DataFrame to JSON (dict format)
        data = df.to_dict(orient="records")

        # 5. Insert into MongoDB
        if len(data) > 0:
            collection.insert_many(data)
            print(f"✅ Inserted {len(data)} documents into '{collection_name}' collection in '{db_name}' database.")
        else:
            print("⚠️ CSV file is empty. Nothing to insert.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    insert_csv_to_mongodb(CSV_FILE_PATH, DATABASE_NAME, COLLECTION_NAME)
