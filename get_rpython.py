import json
import feedparser

target = "http://www.reddit.com/r/Python/.rss"
jre = "http://joshuarenglish.com/feed/"

d = feedparser.parse(jre)
print(type(d))
with open('jre.rss', 'w') as fp:
    json.dump(d, fp)
