import aiohttp
import asyncio
from bs4 import BeautifulSoup
from datetime import datetime
from MailSend import mail_send

# グローバル変数
global_today = ""
# セマフォの設定
semaphore = asyncio.Semaphore(5)  # 同時実行数を制限（例: 5）


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
    # セマフォで同時実行数を制限
    async with semaphore:
        url = f"https://github.com/users/{username}/contributions"
        async with aiohttp.ClientSession() as session:
            html = await fetch(session, url)
            if html:
                soup = BeautifulSoup(html, "html.parser")
                scraping(soup)
        # オプション: サーバーへの負荷を軽減するためのスリープ
        await asyncio.sleep(1)


def scraping(soup):
    contributions = soup.find_all("td", class_="ContributionCalendar-day")
    found_today = False
    contribution_dates = []
    for day in contributions:
        count = int(day.get("data-level"))
        if count > 0:
            date = day.get("data-date")
            if date is not None:
                date = date.strip()
                contribution_dates.append(date)
    contribution_dates.sort()
    print("以下Contributeがある日付のみをソート表示:")
    for date in contribution_dates:
        print(f"{date}")
    for day in contributions:
        date = day.get("data-date")
        if date is not None:
            date = date.strip()
            if date == global_today:
                count = int(day.get("data-level"))
                if count > 0:
                    found_today = True
                break
    if found_today:
        print(f"今日はコントリビューションがあります 日付: {global_today}")
    else:
        print(f"今日はコントリビューションがありません 日付: {global_today}")
        # mail_send()  # メール送信処理
    print("------------------------------------------------")


async def call_contributes(documents):
    tasks = []
    for doc in documents:
        username = doc.get("git_name")
        if username:
            # scrape(..)はすぐに実行されずリストにタスクとして追加されるだけ
            tasks.append(scrape(username))
    if tasks:
        # タスクを並行して実行
        await asyncio.gather(*tasks)


async def get_contribute_main(documents):
    global global_today
    global_today = datetime.today().strftime('%Y-%m-%d')
    print(f"本日の日付は: {global_today}")
    await call_contributes(documents)
