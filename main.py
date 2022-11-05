import tweepy

with open('tokens.txt', 'r') as file:
    f = file.readlines()
    
bToken = f[0].split()[0]
pConToken = f[1].split()[0]
sConToken = f[2].split()[0]
pAuthToken = f[3].split()[0]
sAuthToken = f[4].split()[0]

client = tweepy.Client(bearer_token=bToken)
auth = tweepy.OAuthHandler(pConToken, sConToken) 
auth.set_access_token(pAuthToken, sAuthToken)
api = tweepy.API(auth)



def getFollowers(username: str, numF: int, dec: str):
    for followers in tweepy.Cursor(api.get_followers, screen_name=username, count=numF).pages(3):
        user_followers = str(followers)
        followers = user_followers.split()
        for follower in followers:
            if follower.startswith('screen_name'):
                follower = follower.split("'")[1]
                print(follower)
                #no need to get follower tweets yet. add getTweets(follower) to get 10 recent tweets



def getTweets(f):
    query = f'from:{f} -is:retweet'
    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)
    tweets = str(tweets)
    tweets = tweets.split("=")
    for i in range(len(tweets)):
        tweet = tweets[i]
        if tweet.endswith('text'):
            tweet = tweets[i+1]
            print(tweet[:tweet.find('>')])


def main():
    name = input('Enter the username you want to pull followers from: ')
    num = input('Enter the number of follower names you would like: ')
    wantTweets = input('Would you like to get the 10 most recent tweets from each user?:(yes/no) ')

    getFollowers(name.lower(), num, wantTweets.lower())


main()