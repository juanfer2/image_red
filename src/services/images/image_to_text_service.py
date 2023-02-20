import os
import uuid
import easyocr
import logging
from werkzeug.utils import secure_filename
from src.models.images import Image
from src.repository.image_repository import ImageRepository

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('images_controller')

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def convert_to_text(image, lang):
  extension = image.filename.split('.')[-1:][0]
  filename = f'{str(uuid.uuid4())}.{extension}'
  save_file(image, filename)
  text = read_image(UPLOAD_FOLDER + "/images/" + filename, lang)
  save_db_image(filename=image.filename, uuid=filename, text=text, lang=lang, ext=extension)

  return  {
      'fileName': image.filename,
      'uuid': filename,
      'text': text,
      'lang': lang,
      'ext': extension
  }

def save_file(image, filename):
  target=os.path.join(UPLOAD_FOLDER,'images')
  if not os.path.isdir(target):
    os.mkdir(target)

  destination="/".join([target, filename])
  image.save(destination)

def read_image(path, lang):
  reader = easyocr.Reader([lang], gpu = False)
  results = reader.readtext(path)
  text = ''

  for result in results:
    print("Name...")
    print(result[1])
    print(result[0])
    print(result[0][0])
    print(result[0][1])
    text += result[1] + ' ';

  print(text)

  return text

def save_db_image(filename, uuid, text, lang, ext):
  imageRepo = ImageRepository()
  img = Image(filename=filename, uuid=uuid, text=text, lang=lang, ext=ext)
  imageRepo.create_image(img)
