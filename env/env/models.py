from mongoengine import Document, CASCADE
from mongoengine.fields import ReferenceField, ListField, StringField


class Authors(Document):

    fullname = StringField(required=True)
    born_date = StringField(required=True, max_lenght=30)
    born_location = StringField(required=True, max_length=150)
    description = StringField(required=True)


class Quotes(Document):

    tags = ListField(max_length=10)
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quote = StringField(required=True)
