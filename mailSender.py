import os
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mail_sender_main(user_email):
    # .envファイル読み込み(ローカル用)
    load_dotenv()
    sender_email = os.environ.get("SENDER_EMAIL")
    password = os.environ.get("PASSWORD_EMAIL")

    if sender_email is not None and password is not None:
        mail_sender(sender_email, password, user_email)
    else:
        # エラーを表示する
        print("mailかpasswordが取得できませんでした")
        return "Error: Failed to get E-Mail or AppPassWord", 500


def mail_sender(sender_email, password, user_email):
    # Gmailアカウント情報

    # メールの設定
    receiver_email = user_email
    subject = 'テストメール'
    body = 'これはPythonから送信されたテストメールです。'

    # メールメッセージの作成
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Gmailサーバーへの接続とメール送信
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # 暗号化された接続の開始
        server.login(sender_email, password)
        server.send_message(msg)
        print('メールが送信されました')
    except Exception as e:
        print(f'エラーが発生しました: {e}')
    finally:
        server.quit()
