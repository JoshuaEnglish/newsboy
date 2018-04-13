import code

from create_db import engine, Article, Subscription

code.interact('SQL Playground', local={'e': engine, 'Article': Article,
                                       'Subscription': Subscription})
