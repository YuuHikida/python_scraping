import requests
from bs4 import BeautifulSoup
from datetime import datetime
from MailSend import mail_send

# グローバル変数
global_today = ""


def fetch(url):
    try:
        response = requests.get(url)
        if response.status_code == 404:
            print(f"404エラー: {url} が見つかりません。")
            return None
        elif response.status_code != 200:
            print(f"HTTPエラー {response.status_code}: {url} の処理中にエラーが発生しました。")
            return None
        else:
            return response.text
    except requests.RequestException as e:
        print(f"HTTPエラー: {e}")
        return None


def scrape(username):
    url = f"https://github.com/users/{username}/contributions"
    html = fetch(url)
    if html:
        soup = BeautifulSoup(html, "html.parser")
        scraping(soup)
    # サーバーへの負荷を軽減するためのスリープ（必要に応じて）
    # time.sleep(1)


def scraping(soup):
    contributions = soup.find_all("td", class_="ContributionCalendar-day")
    found_today = False
    contribution_dates = []
    for day in contributions:
        count = int(day.get("data-level", 0))
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
                count = int(day.get("data-level", 0))
                if count > 0:
                    found_today = True
                break
    if found_today:
        print(f"今日はコントリビューションがあります 日付: {global_today}")
    else:
        print(f"今日はコントリビューションがありません 日付: {global_today}")
        # mail_send()  # メール送信処理
    print("------------------------------------------------")


def call_contributes(documents):
    for doc in documents:
        username = doc.get("git_name")
        if username:
            scrape(username)


def get_contribute_main(documents):
    global global_today
    global_today = datetime.today().strftime('%Y-%m-%d')
    print(f"本日の日付は: {global_today}")
    call_contributes(documents)
