from app import app

@app.route('/ping')
def ping():
    return 'pong' 

@app.route('/hello/<name>')
def hello(name):
    return 'Hello, ' + 'Tom'