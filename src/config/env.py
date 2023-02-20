import os
from dotenv import load_dotenv


def load_env():
  load_dotenv()

def get_mongo_url():
  return os.getenv("DATABASE_URL_MONGO")
