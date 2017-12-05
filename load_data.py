import requests
from lxml.html.html5parser import fromstring
r = requests.get('https://twitter.com/cnet')
html = fromstring(r.text)
tweets = html.cssselect('.tweet-text')
for t in tweets:
    print(t.text)