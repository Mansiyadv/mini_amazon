from flask import Flask, send_from_directory, request, Response

app = Flask('mini-amazon', static_url_path='')


@app.route('/health', methods=['GET'])
def health():
    return 'healthy'


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'index.html')


@app.route('/api/products', methods=['POST'])
def products():
    product = dict()
    product['Name'] = request.form['Name']
    product['Description'] = request.form['Description']
    product['Price'] = request.form['Price']
    product['Email ID'] = request.form['Email ID']

    print(product)

    return Response('OK', 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)