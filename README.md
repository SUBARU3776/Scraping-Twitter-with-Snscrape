# Scraping-Twitter-with-Snscrape
#### このPythonスクリプトはTwitter APIを使用せずに、指定されたユーザー（twitter_handle）の最新のツイートをスクレイピングして、それらをCSVファイルに保存するためのものです。
<br>

#### スクリプトの実行手順は次の通りです。

- はじめに必要なライブラリとモジュールをインポートします。
- スクレイピングするTwitterアカウントのtwitter_handle(@hogehoge)を指定します。
- ツイートの属性を格納するための空のリストattributes_containerを作成します。
- スクレイピングする最大ツイート数をmax_tweets = *****に設定します。
- スクレイピング対象のタイムゾーンをUTC+9(日本時間)に設定します。
- ツイートの属性を抽出するための関数scrape_tweetを作成します。
- TwitterSearchScraperを使用して、指定されたユーザーの最新のツイートをスクレイピングします。
- scrape_tweet関数を使用してスクレイピングされた各ツイートの属性をattributes_containerリストに追加します。
- スクレイピングされたツイート属性を使用してPandas DataFrameを作成します。
- DataFrameをCSVファイルに保存します。
- スクレイピングが成功したことを示すメッセージを出力します。

このスクリプトでは、TwitterSearchScraperを使用してツイートを取得しています。<br>TwitterSearchScraperは、Twitter検索結果のページをスクレイピングして、ツイートの属性を取得するためのものです。<br>APIキーなどの認証情報を必要とせず、無料で使用できます。<br>

#### ただし、Twitterがスクレイピングに対して厳しい対策を取る可能性があるため、注意が必要です。

*************************************************************************************************************************************************************************

#### This Python script is designed to scrape the latest tweets of a given user (twitter_handle) and save them to a CSV file without using the Twitter API.<br>

#### The steps to run the script are as follows

- First, import the necessary libraries and modules.
- Specify the twitter_handle (@hogehoge) of the Twitter account to be scraped.
- Create an empty list attributes_container to store the attributes of tweets.
- Set max_tweets = ***** for the maximum number of tweets to be scraped.
- Set the time zone for the scraping target to UTC+9 (Japan time).
- Create a function scrape_tweet to extract the attributes of tweets.
- Use TwitterSearchScraper to scrape the latest tweets of the specified user.
- Add the attributes of each scraped tweet to the attributes_container list using the scrape_tweet function.
- Create a Pandas DataFrame using the scraped tweet attributes.
- Save the DataFrame to a CSV file.
- Output a message indicating that the scraping was successful.
- This script uses TwitterSearchScraper to retrieve tweets.

TwitterSearchScraper is used for scraping Twitter search result pages to obtain the attributes of tweets.
It does not require API keys or other authentication information and is free to use.

However, be aware that Twitter may take strict measures against scraping.
