'''
Este bot fue creado durante un día que renfe se retrasasó
Estaba aburrido en el tren y me puse a hacerlo... grande renfe!

El bot no podría ser más simple, detecta si renfe info ha twiteado algo y si lo
he echo, mira si este tweet contiene al menos una keyword, si es así, procede
a twitear alguna frase estupida.
'''

import config
import tweepy
import time


def has_keyword(text):
    for keyword in keywords:
        if keyword in text.split(' '):
            print("has keyword!")
            return True
    print("does not has keyword")
    return False


def get_last_tweet(api):
    "returns the plain text of the last renfe into tweet"
    return api.user_timeline(screen_name = "riera901", count=1, tweet_mode="extended")[0].full_text


def a_new_train_is_delayed(api):
    global tweet
    "retuns true when renfe info tweets something that contains at least 1 delay keyword"
    if tweet != get_last_tweet(api):
        print("new tweet!!")
        tweet = get_last_tweet(api)
        if has_keyword(tweet):
            return True
    return False


def tweet_content(api, content):
    "tweets a string!"
    print(content)


def pooling(api):
    "just the polling. Again and again and again..."
    print("pooling...")
    if a_new_train_is_delayed(api):
        content = "Capitán Renfe se retrasa de nuevo!"
        tweet_content(api, content)


def main():
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    api = tweepy.API(auth)
    global tweet
    global keywords
    tweet = get_last_tweet(api)
    keywords = open("keywords.dat", "r").read().split(' ')
    
    print (keywords)
    print (tweet)
    
    
    while True:
        try:
            time.sleep(1)
            pooling(api)
            time.sleep(1)
        except Exception as e:
            print("an exception has occured, but don't ask me to fix it :)")
            print(e)

if __name__ == '__main__':
    main()


#    __
# __( o)>
# \ <_ ) r90