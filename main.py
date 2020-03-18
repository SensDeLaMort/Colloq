import vk_api
from settings import *
from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello from Flask!'


@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    elif data['type'] == 'confirmation':
        return CONFIRM_TOKEN
