import redis
import json

r = redis.StrictRedis(host="redis", port=6379, db=0)

# pr les noms de produits il faut d'abord utiliser un genre de process EMR
# afin d'avoir des noms faciles a traiter
# (car il ny a aucune coherence dans les noms et cela ne facilite pas linsertion dans redis ni la recuperation de linfo)

MAX_PREFIX_LENGTH = 50 # taille limite des prefixes a inserer

print "Loading entries in the Redis DB\n"

with open('products.json',"r") as f:
    products = json.load(f)
    for product in products:
        n = product["name"]
        if n:
            prefix_len = min(len(n), MAX_PREFIX_LENGTH)
            for c in range(1,prefix_len):
                prefix = n[0:c]
                r.zadd('names',0,prefix)
            r.zadd('names',0,n+"*")

