import json
import code

with open('jre.rss', 'r') as fp:
    d = json.load(fp)

code.interact("Newsboy Playground", local={'d': d})
