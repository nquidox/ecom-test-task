import os.path

from tinydb import TinyDB


class dbworker:
    dbname = "templates.json"

    def connect(self) -> TinyDB:
        return TinyDB(self.dbname)

    def get_all_templates(self) -> list:
        db = self.connect()
        return db.all()

    def init_data(self):
        if not os.path.exists(self.dbname):
            db = self.connect()
            db.insert({"username_only":
                           {"name": "string"}})
            db.insert({"user_info":
                           {"name": "string", "date": "date", "email": "email", "phone": "phone"}})
            db.insert({"user_more_info":
                           {"name": "string", "date": "date", "email": "email", "phone": "phone", "address": "string"}})
            db.insert({"user_maximum_info":
                           {"name": "string", "date": "date", "email": "email", "phone": "phone", "address": "string",
                            "age": "number"}})
