import json
from pymongo import MongoClient

client = MongoClient('mongo:27017')
db = client.test.products

print "Loading entries in the Mongo DB\n"

with open('products.json', 'r') as f:
    products = json.load(f)
    for product in products:
        db.insert_one({
            "sku":product.get("sku", None),
            "name":product.get("name", None),
            "type":product.get("type", None),
            "price":product.get("price", None),
            "upc":product.get("upc", None),
            "category":product.get("category", None),
            "shipping":product.get("shipping", None),
            "description":product.get("description", None),
            "manufacturer":product.get("manufacturer", None),
            "model":product.get("model", None),
            "url":product.get("url", None),
            "image":product.get("image", None)
            })
