import pandas as pd
import matplotlib.pyplot as plt
import calendar
import random

# データを読み込み、Date Createdを日時型に変換する
df = pd.read_csv('D:\Python\snscrape\snscrape_sksk0873k777_tweets_2023-04-15 14.24.57.csv')
df['Date Created'] = pd.to_datetime(df['Date Created'])

# データの最新日を取得する
latest_date = df['Date Created'].max()

# 投稿日と投稿時間を分離する
df['date'] = df['Date Created'].dt.date
df['hour'] = df['Date Created'].dt.hour

# 日付が30日以内のデータを抽出する
cutoff = latest_date.normalize() - pd.Timedelta(days=29)
counts = df[df['Date Created'] >= cutoff].groupby(['date', 'hour', 'source']).size().reset_index(name='count')

# source毎の投稿数をカウントする
source_counts = df[df['Date Created'] >= cutoff].groupby(['source']).size().reset_index(name='total_count')

# 投稿件数の降順でソートする
source_counts = source_counts.sort_values(by=['total_count'], ascending=False)

# ソースごとの割合を計算する
source_counts['percentage'] = source_counts['total_count'] / source_counts['total_count'].sum() * 100

# 小数点以下第2位で四捨五入する
source_counts['percentage'] = source_counts['percentage'].round(2)

# sourceカラムの文字を左揃えにして幅を合わせる
width = 20
source_counts['source'] = source_counts['source'].apply(lambda x: x.ljust(width))

# 結果を出力する
print(source_counts.to_string(index=False, index_names=False, justify='center'))

# sourceに応じてランダムな色を割り当てる
sources = counts['source'].unique()
color_map = {}
for source in sources:
    color_map[source] = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
counts['color'] = counts['source'].map(lambda x: color_map[x])

# グラフの描画領域を設定する
fig, ax = plt.subplots(figsize=(11,7))

# y軸に曜日と日付を設定する
dates = pd.date_range(start=cutoff, end=latest_date, freq='D')
weekdays = [calendar.day_name[d.weekday()] for d in dates]
labels = [f'{w[:3]} {d.strftime("%m/%d")}' for d, w in zip(dates, weekdays)]
ax.set_yticks(dates)
ax.set_yticklabels(labels)

# "Sun"のラベルを赤色にする
sun_indices = [i for i, label in enumerate(labels) if "Sun" in label]
for i in sun_indices:
    ax.get_yticklabels()[i].set_color("red")

# sourceごとにラベルと色を設定する
for source, color in color_map.items():
    data = counts[counts['source'] == source]
    ax.scatter(data['hour'], data['date'], s=data['count']*50, alpha=0.5, c=color, label=source) # マーカーの大きさを決定

# 凡例を追加する
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='center left', bbox_to_anchor=(1.0, 0.5))

# x軸のラベルと範囲を設定する
ax.set_xlabel('Hour of the day')
ax.set_xlim(-0.5, 23.5)
ax.set_xticks(range(0, 24))

# x軸のグリッド線を追加する
ax.xaxis.grid(True)

# y軸の範囲を設定する
ax.set_ylim(cutoff - pd.Timedelta(hours=12), latest_date + pd.Timedelta(hours=12))

# y軸のグリッド線を追加する
ax.yaxis.grid(True)

# グラフのタイトルを設定する
ax.set_title('Tweet activity over time')

plt.show()