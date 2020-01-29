import tweepy
import time

# include the API Key
auth = tweepy.OAuthHandler(‘APIKEY’, ‘APIKEYSECRET’)

# access token and access token
auth.set_access_token(‘SAT’, ‘SATP’)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

# show user
# print(user)

# show user screen name
# print(user.screen_name)

# Shows the followers for this twitter account using cursor
# for follower in tweepy.Cursor(api.followers).items():
#     print(follower.name)

# follow back a follower
# for follower in tweepy.Cursor(api.followers).item():
#     if follower.name == '':
#         follower.follow()

# gather search terms and number
search = 'Javascript'
nrTweets = 50

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# to retweet a tweet
# for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
#     try:
#         print('Retweeted')
#         tweet.retweet()
#         time.sleep(10)
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break
