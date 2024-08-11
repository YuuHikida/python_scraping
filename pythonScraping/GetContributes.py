import aiohttp
import asyncio
from bs4 import BeautifulSoup
from datetime import datetime

# 本日の日付(グローバル変数)
global_today = ""


async def fetch(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 404:
                print(f"404エラー: {url} が見つかりません。")
                return None
            elif response.status != 200:
                print(f"HTTPエラー {response.status}: {url} の処理中にエラーが発生しました。")
                return None
            else:
                html = await response.text()
                return html
    except aiohttp.ClientError as e:
        print(f"HTTPエラー: {e}")
        return None


async def scrape(username):
    url = f"https://github.com/users/{username}/contributions"
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            # スクレイピング処理（ここに処理を書く）
            # 例えば、soupから情報を抽出して何かをする
            # data = soup.find(...)  # 例
            # process(data)  # 例


async def call_contributes(documents):
    tasks = []
    for doc in documents:
        username = doc.get("git_name")
        if username:  # usernameがNoneでない場合
            tasks.append(scrape(username))

    if tasks:
        await asyncio.gather(*tasks)


# main.py から呼び出されるように
async def main(documents):
    global global_today
    global_today = datetime.today().strftime('%Y-%m-%d')
    print(f"本日の日付は: {global_today}")
    await call_contributes(documents)

# def call_contributes(documents):
#     for doc in documents:
#         # GitHubのユーザー名
#         username = doc.get("git_name")
#         url = "https://github.com/users/" + username + "/contributions"
#         response = request.urlopen(url)
#
#         # BeautifulSoup初期化
#         soup = BeautifulSoup(response, "html.parser")
#         response.close()
#
#         # 現在の日付を取得 (YYYY-MM-DDの形式)
#         today = datetime.today().strftime('%Y-%m-%d')
#         print(f"本日の日付は: {today}")
#
#         # コントリビューション情報を抽出
#         contributions = soup.find_all("td", class_="ContributionCalendar-day")
#
#         # 今日のコントリビューションがあったかどうかを示すフラグ
#         found_today = False
#
#         # 各日付毎にコントリビューション数を確認
#         contribution_dates = []
#
#         # contributeがある日だけリストに入れる
#         for day in contributions:
#             count = int(day.get("data-level"))
#             if count > 0:
#                 date = day.get("data-date")
#                 if date is not None:
#                     date = date.strip()
#                     # 日付をリストに追加
#                     contribution_dates.append(date)
#
#         # 日付をソート
#         contribution_dates.sort()
#         print("以下Contributeがある日付のみをソート表示:")
#         for date in contribution_dates:
#             print(f"{date}")
#
#         # 本日のContributeがあったか表示
#         for day in contributions:
#             date = day.get("data-date")
#             if date is not None:
#                 date = date.strip()
#                 # 日付をリストに追加
#                 # contribution_dates.append(date)
#                 if date == today:
#                     # contributeを取得
#                     count = int(day.get("data-level"))
#                     if count > 0:
#                         found_today = True
#                     break  # 今日の日付を見つけたらループを抜ける
#
#         # 今日のコントリビューションがあったかどうかを表示
#         if found_today:
#             print(f"今日はコントリビューションがあります 日付: {today}")
#         else:
#             print(f"今日はコントリビューションがありません 日付: {today}")
#             # 以下　DBからidをjavaプログラムへ飛ばす
#             # 暫定的にpythonのmail送信機能を使う
#             mail_send()
#         print("------------------------------------------------")
