from flask import Flask, request


app = Flask(__name__)

app.config.from_pyfile('config.py')

from resource import *

if __name__ == '__main__':
    app.run(debug=True)