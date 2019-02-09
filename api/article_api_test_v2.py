from aylienapiclient import textapi
from unidecode import unidecode
import string

class Analyze():
	text = ""
	def __init__(self, text):
		self.text = text
	def analyze(self):
		return self.text

def clean_body(body_str):
	body_str = str(body_str.lower().encode("utf-8"))
	printable = set(string.printable)
	body = " ".join(body_str.split())
	body = filter(lambda x: x in printable, body)
	
	return body

def convert(url="https://www.theverge.com/2019/2/8/18217174/jeff-bezos-blackmail-leaked-photos-national-enquirer-donald-trump-extortion-ami-explainer"):
	client = textapi.Client("6d2ea87b", "3dc27a2f57baea46d4882adb000bae8b")
	extract = client.Extract({"url": url, "language": True})
	body = extract["article"]
	cleanedBody = clean_body(body)
	analyzedExtract = Analyze(cleanedBody).analyze()
	return analyzedExtract
