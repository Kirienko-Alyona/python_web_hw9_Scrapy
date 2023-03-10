import re

from pymongo import MongoClient
from termcolor import colored
import redis
from redis_lru import RedisLRU

from decor import input_error
from models import Quotes, Authors
from connect import conn


client_redis = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client_redis)

@cache
@input_error
def return_quote(quote: Quotes) -> str:
    quote = quote.quote
    client_redis.set("quote", quote)
    client_redis.get("quote")
    return quote


@input_error
def search_name(fullname: list) -> list: 
    name = (fullname[0].split(" "))[0]
    try:
        author = Authors.objects(fullname__istartswith=name).first() #istartswith -поле рядка починається зі значення (незалежно від регістру)
        list_quote = Quotes.objects(author=author.id)
    except AttributeError:
        return colored("Can't find quote of this author or the tag.", "red")
    return list_quote
        
        
@input_error
def search_tag(data: list) -> list:
    list_quote = []
    for item in data:
        if (item.find(" ") != -1) or (item.islower() == False):
            raise KeyError(colored("Wrong format. Please enter: '{command:}{tag,tag}' without spaces in lower case.", "red"))
        regexpr = re.compile('^'+ item)
        quote = Quotes.objects(tags__iregex=regexpr).first() #iregex – поле рядка збігається з регулярним виразом (незалежно від регістру)
        if quote == None:
            raise AttributeError(colored("Can't find quote of this author or the tag.", "red"))
        list_quote.append(quote)
    return list_quote


if __name__ == '__main__':

    client = MongoClient(conn)
    db = client.mongo_db
    client.close()
