import os
from urllib import request
from bs4 import BeautifulSoup

# usernameをmysqlから取得
username = "YuuHikida"
url = "https://github.com/users/" + username + "/contributions"
response = request.urlopen(url)

# BeautifulSoup初期化
soup = BeautifulSoup(response, "html.parser")
response.close()

# コントリビューション情報を抽出
contributions = soup.find_all("td", class_="ContributionCalendar-day")

# 各日付毎にコントリビューション数を取得してリストに追加
contrib_list = []
#　以下はリスト
for day in contributions:
    date = day.get("data-date")
    count = day.get("data-level")  # data-levelはコントリビューション数のレベルを表す
    if int(count) > 0:  # コントリビューションがあった場合
        contrib_list.append((date, count))

# 日付順にソート
contrib_list.sort(key=lambda x: x[0])

# ソートされたコントリビューション情報を表示
print("contributions:")
for date, count in contrib_list:
    print(date, ":", count)
