#!/usr/bin/python3
import json
import urllib.parse

from flask import Flask
from flask import request

from .api import API

app = Flask(__name__)


@app.route('/analyze')
def analyze():
	url = urllib.parse.unquote(request.args.get('url'))

	article = API.extract_article(url)
	analysis = API.analyze(article)

	return json.dumps(analysis)
