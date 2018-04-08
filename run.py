from flask import Flask, send_from_directory, request, Response

app = Flask('mini-amazon', static_url_path='')
product_list = []


@app.route('/health', methods=['GET'])
def health():
    return 'healthy'


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'index.html')


@app.route('/api/products', methods=['POST', 'GET'])
def products():
    if request.method == 'GET':
        print(product_list)
        print(request.args['Name'])
        for product in product_list:
            if product['Name'] == request.args['Name']:
                return Response(str(product), 200)
        return Response(str({}), 200)
    elif request.method == 'POST':
        product = dict()
        product['Name'] = request.form['Name']
        product['Description'] = request.form['Description']
        product['Price'] = request.form['Price']
        print(product)

        product_list.append(product)

        return Response('OK', 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
