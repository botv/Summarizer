from aylienapiclient import textapi
import string
from .analyze import Analyze

class ArticleAPI:
	@staticmethod
	def clean_body(body_str):
		body_str = str(body_str.lower().encode('utf-8'))
		printable = set(string.printable)
		body = ' '.join(body_str.split())
		body = filter(lambda x: x in printable, body)

		return body

	@staticmethod
	def convert(url='https://www.theverge.com/2019/2/8/18217174/jeff-bezos-blackmail-leaked-photos-national-enquirer-donald-trump-extortion-ami-explainer'):
		client = textapi.Client('6d2ea87b', '3dc27a2f57baea46d4882adb000bae8b')
		extract = client.Extract({'url': url, 'language': True})
		body = extract['article']
		cleanedBody = ArticleAPI.clean_body(body)
		analyzedExtract = Analyze.analyze(cleanedBody)
		return analyzedExtract
