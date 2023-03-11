from app import app
from flask import request

@app.route('/ping')
def ping():
    return 'pong' 

@app.route('/hello/<name>')
def hello(name):
    return 'Hello, ' + 'Tom'

@app.route('/json', methods=['GET'])
def json():
    # returns {'success': True, 'email': xxx@xxx.com, 'password': 'xxx'}
    args = request.args
    email = args.get('email')
    password = args.get('password')

    if not '@' in email: 
        return {'success': False, 'error': 'Invalid email'}
    
    return {'success': True, 'email': email, 'password': password}