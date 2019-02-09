from flask import Flask
from flask import request
from .article_api import ArticleAPI
import json

app = Flask(__name__)

@app.route('/convert')
def hello_world():
	url = request.args.get('url')
	result = ArticleAPI.convert(url)

	return json.dumps(result)