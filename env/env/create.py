import json
from pymongo import MongoClient

from models import Authors, Quotes
from connect import conn

filenames = ["authors", "quotes"]


def create_collection():
    for filename in filenames:
        db[filename]
        path = filename + ".json"

        with open(path, encoding="utf-8") as f:
            text = f.read()
            myList = json.loads(text)
            for jsonObj in myList:
                if filename == "authors":
                    authors = Authors(fullname=jsonObj['fullname'], born_date=jsonObj["born_date"],
                                     born_location=jsonObj["born_location"], description=jsonObj["description"])
                    authors.save()
                elif filename == "quotes":
                    authors = Authors.objects(fullname=jsonObj["author"])
                    quotes = Quotes(tags=jsonObj["tags"], author=authors[0].id, quote=jsonObj["quote"])
                    quotes.save()
    return


if __name__ == '__main__':

    client = MongoClient(conn)
    db = client.mongo_db
    create_collection()
    client.close()
