__version__ = '0.1.0'

from flask import Flask, escape, request

application = Flask(__name__)

@application.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'