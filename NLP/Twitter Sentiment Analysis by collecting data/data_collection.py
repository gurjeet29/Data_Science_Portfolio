# Python Script to Extract tweets of a
# particular Hashtag using Tweepy and Pandas

# import modules
import pandas as pd
import tweepy

# function to display data of each tweet


def printtweetdata(n, ith_tweet):
    print()
    print(f"Tweet {n}:")
    print(f"Description:{ith_tweet[0]}")


# function to perform data extraction
def scrape(words, date_since, numtweet):

    # Creating DataFrame using pandas
    db = pd.DataFrame(columns=['description'])

    # We are using .Cursor() to search
    # through twitter for the required tweets.
    # The number of tweets can be
    # restricted using .items(number of tweets)
    tweets = tweepy.Cursor(api.search_tweets,
                           words, lang="en",
                           since_id=date_since,
                           tweet_mode='extended').items(numtweet)

    # .Cursor() returns an iterable object. Each item in
    # the iterator has various attributes
    # that you can access to
    # get information about each tweet
    list_tweets = [tweet for tweet in tweets]

    # Counter to maintain Tweet Count
    i = 1

    # we will iterate over each tweet in the
    # list for extracting information about each tweet
    for tweet in list_tweets:
        description = tweet.user.description

        # Here we are appending all the
        # extracted information in the DataFrame
        ith_tweet = [description]
        db.loc[len(db)] = ith_tweet

        # Function call to print tweet data on screen
        printtweetdata(i, ith_tweet)
        i = i+1
    filename = 'data.csv'

    # we will save our database as a CSV file.
    db.to_csv(filename)


if __name__ == '__main__':

    # Enter your own credentials obtained
    # from your developer account
    consumer_key = "XXXXXXXXXXXXXXX"
    consumer_secret = "XXXXXXXXXXXXXXXXXXX"
    access_key = "XXXXXXXXXXXXX-XXXXXXXXXXX"
    access_secret = "XXXXXXXXXXXXXXXXXXXX"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Enter Hashtag and initial date
    print("Enter Twitter HashTag to search for")
    words = input()
    print("Enter Date since The Tweets are required in yyyy-mm--dd")
    date_since = input()

    # number of tweets you want to extract in one run
    numtweet = 1500
    scrape(words, date_since, numtweet)
    print('Scraping has completed!')
