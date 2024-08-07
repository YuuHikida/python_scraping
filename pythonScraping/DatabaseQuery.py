import MySQLdb
from GetContributes import call_contributes


def db_call():
    # ここでdbからメールをコール
    # 今は全権取得予定
    # 一番いいのは１日のはじめに全件取得し、リストにデータを格納しておき
    # 上記を元にメールを送る方法

    # DBに入っている全ユーザーの"username"を取得して回す
    # connectionオブジェクトを作成した時点でDBに接続している
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='1121',
        db='my_database'

    )
    # cursorはDBと対話する関数
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM my_table")
    # タプルで格納されるs
    results = cursor.fetchall()
    first_last_name = results[0][0]
    second_name = results[1][0]
    print(first_last_name)  # 'HIKIDA'
    print(second_name)

    # 接続を閉じる
    cursor.close()
    connection.close()

    call_contributes()
