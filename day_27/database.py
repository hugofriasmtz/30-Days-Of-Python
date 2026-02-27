from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

try:
    client = MongoClient(MONGODB_URI)
    client.admin.command("ping")
    print("Conectado a MongoDB Atlas")

    db = client["thirty_days_of_python"]

except Exception as e:
    print("Error de conexión:", e)