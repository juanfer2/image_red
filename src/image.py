import easyocr

def read_image(path, lang):
  reader = easyocr.Reader([lang])
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
