class Image:
    def __init__(self, uuid, filename, ext, lang, text):
        self.uuid = uuid
        self.filename = filename
        self.ext = ext
        self.lang = lang
        self.text = text

    def toDBCollection(self):
        return {
            "ext": self.ext,
            "filename": self.filename,
            "lang": self.lang,
            "uuid": self.uuid,
            "text": self.text
        }
