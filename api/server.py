from flask import Flask
from flask import request
from aylienapiclient import textapi
from article_api_test_v2 import *
import json 

app = Flask(__name__)

@app.route('/convert')
def hello_world():
	url = request.args.get('url')
	return json.dumps(convert(url))