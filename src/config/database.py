from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

def conn():
  try:
    client = MongoClient('mongodb://localhost:27017')
    db = client["image_red"]
    print('Connexión succesfully')
  except ConnectionError:
    print('Error de conexión con la bdd')
  return db
#todos = db.todos
