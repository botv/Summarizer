import requests
import json
# token = 1aad7dd6e296d3047f8df4dce94418d0

params={"token": '1aad7dd6e296d3047f8df4dce94418d0',
		"url": 'https://www.theverge.com/2019/2/8/18217174/jeff-bezos-blackmail-leaked-photos-national-enquirer-donald-trump-extortion-ami-explainer',
		}


url = 'https://api.diffbot.com/v3/article'

r = requests.get('https://api.diffbot.com/v3/article',params=params)

data = r.json()

print data['objects'][0]['text']
