import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime
import os
import requests.exceptions
from concurrent.futures import ThreadPoolExecutor

# Change CWD
os.chdir('D:\Python\snscrape')

# Set the Twitter handle to search for
twitter_handle = "from:Hidetoshi_H_"

# Extract the handle from the search query for use in the file name
handle = twitter_handle.split(":")[1]

# Created a list to append all tweet attributes(data)
attributes_container = []

# Set the max number of tweets to scrape
max_tweets = 5000

# Set the time zone offset to UTC+9
utc_offset = datetime.timedelta(hours=9)

def scrape_tweet(tweet):
    # Convert tweet.date to UTC+9 timezone and desired format
    tweet_date = (tweet.date + utc_offset).strftime("%Y/%m/%d %H:%M:%S")

    # Append converted tweet date to attributes container list
    attributes_container.append([tweet_date, tweet.id, tweet.user.id, tweet.user.username, tweet.likeCount, tweet.retweetCount, tweet.replyCount, tweet.viewCount, tweet.sourceLabel, tweet.rawContent])

# Using TwitterSearchScraper to scrape data and append tweets to list
try:
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(twitter_handle).get_items()):
            if i >= max_tweets:
                break

            futures.append(executor.submit(scrape_tweet, tweet))

            # Add progress counter
            if (i+1) % 1000 == 0:
                print(f"Progress: {i+1}")

        # Wait for all futures to complete
        for future in futures:
            future.result()

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    print(f"Error details: {e.__dict__}")
    # Exit program or do some error handling here

except Exception as e:
    print(f"An error occurred while scraping tweets: {e}")
    # Exit program or do some error handling here

# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(attributes_container, columns=["Date Created", "Tweet Id", "ID", "user_name", "like_count", "retweet_count", "reply_count", "impression_count", "source", "Tweets"])

# Remove newline characters from the "Tweets" column
tweets_df["Tweets"] = tweets_df["Tweets"].str.replace('\n', '')

# Save dataframe to csv
try:
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H.%M.%S")
    filename = f"snscrape_{handle}_tweets_{timestamp}.csv"
    tweets_df.to_csv(filename, index=False)
    print(f"Tweets saved to file: {filename}")

except Exception as e:
    print(f"An error occurred while saving tweets to file: {e}")
    # Exit program or do some error handling here
    print(f"Tweets saved to file: {filename}")

# Print success message
print(f"Scraping of {twitter_handle} completed successfully! {len(attributes_container)} tweets scraped and saved to {filename}")
