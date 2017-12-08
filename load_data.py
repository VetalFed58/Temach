import requests
from lxml.html.html5parser import fromstring
from lxml import etree
import re

from django.contrib.auth.models import User
from blog.models import Post
from datetime import datetime

def post_tweets(account):
    cnet = User.objects.all()[13]

    for tweet in get_tweets(account):
        p = Post(author=cnet, topic = 'technologies', text=tweet, published_date = datetime.now())
        p.save()


def get_tweets(account):
    r = requests.get('https://twitter.com/' + account)
    html = fromstring(r.text)
    tweets = html.cssselect('.tweet-text')
    for t in tweets:
        text = etree.tostring(t).decode('utf-8')
        text = re.sub('<[^>]+>', '', text)
        text = re.sub('http[^ ]+', '', text)
        yield text