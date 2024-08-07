import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mail_send():
    # SMTPサーバーの設定
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "ponponda0103@gmail.com"
    sender_password = "uolt lsgs vsxq frlp"

    # メールの構成
    # ここをDBからmailを全取得する
    receiver_email = "ponponda0103@example.com"
    subject = "テストメール"
    body = "これはPythonから送信されたテストメールです。"

    # MIMEマルチパートメッセージの設定
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # SMTPサーバーに接続しメールを送信
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # TLS（Transport Layer Security）の開始
        server.login(sender_email, sender_password)  # ログイン
        server.sendmail(sender_email, receiver_email, msg.as_string())  # メールを送信
        print("メールが送信されました！")
    finally:
        server.quit()  # サーバーから切断

