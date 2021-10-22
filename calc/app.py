# Put your app in here.
from flask import Flask, request
import operations
app = Flask(__name__)


@app.route('/add')
def adding():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(operations.add(a, b))


@app.route('/sub')
def substract():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(operations.sub(a, b))


@app.route('/mult')
def multiply():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(operations.mult(a, b))


@app.route('/div')
def divide():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(operations.div(a, b))


