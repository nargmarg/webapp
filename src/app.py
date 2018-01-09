import redis
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask,render_template,jsonify,json,request,redirect,url_for
## TODO add code to get product name from MongoDB and fill up Redis with it

application = Flask(__name__)

client = MongoClient('mongo:27017')
db = client.test.products

r = redis.StrictRedis(host="redis", port=6379, db=0)

def getProduct(key):
    try:
        productObject = db.find_one({'name':key})
        productDict = {
                'name':productObject['name'],
                'model':productObject['model'],
                'sku':productObject['sku'],
                'type':productObject['type'],
                'description':productObject['description'],
                'price':productObject['price'],
		'image':productObject['image']
                }
        return productDict
    except Exception, e:
        return str(e)

@application.route('/search/<query>', defaults={'page': 1}, methods=['GET', 'POST'])
@application.route('/search', methods=['GET', 'POST'])
def search(page,query): #FIXME
    if request.method != 'POST':
        result = []
        results = {"results": result.append({"name":i}) for i in autocomplete(query)}
        results = {"results": result}

        if query:
            return jsonify(results)
    else:
        product = getProduct(query)
        return jsonify(product)

def autocomplete(query):
    count = 50
    results = []
    rangelen = 50 # This is not random, try to get replies < MTU size
    start = r.zrank('names',query)

    if start is None:
        return []

    while (len(results) != count):
        range = r.zrange('names',start,start+rangelen-1)
        start += rangelen

        if not range or len(range) == 0:
            break

        for entry in range:
            minlen = min(len(entry),len(query))
            if entry[0:minlen] != query[0:minlen]:
                count = len(results)
                break

            if entry[-1] == "*" and len(results) != count:
                results.append(entry[0:-1])

    return results

@application.route('/show/<product_name>')
def showProduct(product_name):
    product = getProduct(product_name)
    return render_template('index.html')

@application.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0')
