from flask import Flask
from flask_cors import CORS, cross_origin
from src.routes.route import register_routes
from src.config.env import load_env, get_mongo_url
from src.models.images import Image
from src.repository.image_repository import ImageRepository

app = Flask(__name__)
CORS(app, expose_headers='Authorization')
register_routes(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
