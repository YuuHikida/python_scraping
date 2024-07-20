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

# HTMLの内容をプリティプリント
print(soup.prettify())
