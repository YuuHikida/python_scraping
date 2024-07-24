import os
from urllib import request
from bs4 import BeautifulSoup
from datetime import datetime
def callJavaFile():
    #ここでjavafileをコール
    print("JavaFileをcall")
def main():
    #DBに入っている全ユーザーの"username"を取得して回す
    # GitHubのユーザー名
    username = "YuuHikida"
    url = "https://github.com/users/" + username + "/contributions"
    response = request.urlopen(url)

    # BeautifulSoup初期化
    soup = BeautifulSoup(response, "html.parser")
    response.close()

    # 現在の日付を取得 (YYYY-MM-DDの形式)
    today = datetime.today().strftime('%Y-%m-%d')
    print(f"Today's date: {today}")

    # コントリビューション情報を抽出
    contributions = soup.find_all("td", class_="ContributionCalendar-day")

    # 今日のコントリビューションがあったかどうかを示すフラグ
    found_today = False

    # 各日付毎にコントリビューション数を確認
    for day in contributions:
        date = day.get("data-date")
        if date is not None:
            date = date.strip()
            if date == today:
                # contributeを取得
                count = int(day.get("data-level"))
                if count > 0:
                    found_today = True
                break  # 今日の日付を見つけたらループを抜ける

    # 今日のコントリビューションがあったかどうかを表示
    if found_today:
        print(f"今日はコントリビューションがあります 日付: {today}")
    else:
        print(f"今日はコントリビューションがありません 日付: {today}")
        #以下　DBからidをjavaプログラムへ飛ばす

if __name__ == "__main__":
    main()