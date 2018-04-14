from flask import Flask, send_from_directory, request, Response
import pymongo
from pymongo import MongoClient

client= MongoClient('localhost',27017)
db= client.mini_amazon

app = Flask('mini-amazon', static_url_path='')
#product_list = []


@app.route('/health', methods=['GET'])
def health():
    return 'healthy'


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'index.html')


@app.route('/api/products', methods=['POST', 'GET'])

def products():
    if request.method == 'GET':
        #print(product_list)
        #print(request.args['name'])
        match_prod=db.products.find({'Name':  request.args['Name']})
        matches=[]

        for prod in match_prod:
            matches.append(prod)
               
        return Response(str(matches), mimetype="application/json", status=200)
    elif request.method == 'POST':
        product = dict()
        product['Name'] = request.form['Name']
        product['Description'] = request.form['Description']
        product['Price'] = request.form['Price']
        #print(product)

        db.products.insert_one(product)

        return Response(str({'status':'success'}), mimetype="application/json", status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

json_obj = {'Name':''}