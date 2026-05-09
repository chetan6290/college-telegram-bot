from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

ADMIN_ID = int(os.getenv("ADMIN_ID"))

DB_NAME = "college_bot"