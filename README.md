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
