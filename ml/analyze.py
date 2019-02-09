import requests
from aylienapiclient import textapi

class Analyze(object):

    def __init__(self, text):
        self.text = text

    def analyze(self):
        client = textapi.Client('6d2ea87b','3dc27a2f57baea46d4882adb000bae8b')
        sentiment = client.Sentiment({'text':'John is a football player! He is from South Carolina, and plays on the state team!When he gets older he wants to play in the NFL. While he understands that you can get hurt in hte nfl his passionn is greater than the possible physical pain'})
        summary = client.Summarize({'text':'John is a very good football player! He is from South Carolina, and plays on the state team! When he gets older he wants to play in the NFL. While he understands that you can get hurt in hte nfl his passionn is greater than the possible physical pain','title':'fill'})
        del sentiment['text']
        del summary['text']
        returnDic = {'sentiment':sentiment,'summary':summary}
        return returnDic


analysis = Analyze('hello').analyze()
