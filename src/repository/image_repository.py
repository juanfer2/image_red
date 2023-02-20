from src.config.database import conn
from src.models.images import Image

class ImageRepository:
  def __init__(self):
    db = conn()
    self.db = db['images']

  def create_image(self, image=Image):
    return self.db.insert_one(image.toDBCollection())

  def all(self):
    return self.db.find()
    
