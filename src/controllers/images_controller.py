from flask import jsonify, request
from flask_restplus import Namespace, Resource
from src.services.images.image_to_text_service import convert_to_text
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('images_controller')

api = Namespace('images', description='Images Endpoints')

@api.route('/')
class ImagesController(Resource):
    @api.doc('Set Images')
    def get(self):
        print('Image....')
        return jsonify({'data': 'images'})

@api.route('/convert')
class ImagesProcessController(Resource):
    @api.doc('Convert Images')
    def post(self):
        print('Convert Image....')
        file = request.files['image']
        body = request.form
        lang = body.get('lang')
        data = convert_to_text(file, lang)

        return jsonify(data)

