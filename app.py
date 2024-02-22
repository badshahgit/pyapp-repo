# app.py

from flask import Flask

app = Flask(__name__)

# Route to the root URL
@app.route('/')
def hello():
    return 'Welcome to elai agritech!'

# Route to a custom endpoint
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}! Welcome to ELAI AGRI tech!.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
