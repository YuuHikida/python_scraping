#参考　https://corgi-lab.com/diary/github-weekly-grass/

from urllib import request
from bs4 import BeautifulSoup

# usernameをmysqlから取得
username = "YuuHikida"
url = "https://github.com/users/" + username + "/contributions"
response = request.urlopen(url)

# BeautifulSoup初期化
soup = BeautifulSoup(response, "html.parser")
response.close()
print("aaaa")
# コントリビューション情報を抽出
contributions = soup.find_all("rect", class_="day")

# 各日付毎にコントリビューション数を表示
print(contributions)
for day in contributions:
    date = day.get("data-date")
    count = day.get("data-count")
    print(date, ":", count)