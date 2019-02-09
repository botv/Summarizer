from aylienapiclient import textapi

class Analyze():
	text = ""
	def __init__(self, text):
		self.text = text
	def analyze(self):
		return self.text

def convert(url):
	client = textapi.Client("6d2ea87b", "3dc27a2f57baea46d4882adb000bae8b")
	# url = "https://www.theverge.com/2019/2/8/18217174/jeff-bezos-blackmail-leaked-photos-national-enquirer-donald-trump-extortion-ami-explainer"
	extract = client.Extract({"url": url, "language": True})
	body = extract["article"]
	analyzedExtract = Analyze(body).analyze()
	return analyzedExtract
