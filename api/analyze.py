from aylienapiclient import textapi

class Analyze:
	@staticmethod
	def analyze(text):
		client = textapi.Client('6d2ea87b', '3dc27a2f57baea46d4882adb000bae8b')
		sentiment = client.Sentiment({'text': text})
		summary = client.Summarize({'text': text, 'title': 'fill'})
		del sentiment['text']
		del summary['text']
		return {'sentiment': sentiment, 'summary': summary}
