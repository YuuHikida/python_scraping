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
