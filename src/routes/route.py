from flask import Blueprint
from flask_restplus import Api
from werkzeug.exceptions import HTTPException

from src.controllers.images_controller import api as images_controller

blueprint = Blueprint('images', __name__, url_prefix='/api/v1')

api = Api(blueprint,
          doc='/doc/',
          title='Resource API - Images',
          version='1.0',
          description='A description'
          )

@api.errorhandler(HTTPException)
def handle_error(error: HTTPException):
    """ Handle BluePrint JSON Error Response """
    response = {
        'error': error.__class__.__name__,
        'message': error.description,
    }
    return response, error.code

api.add_namespace(images_controller)


def register_routes(app):
    """
    Register routes with blueprint and namespace
    """
    app.register_blueprint(blueprint)
