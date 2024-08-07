import MySQLdb
from Get_contributes import call_contributes


def call_java_file():
    # ここでjava_fileをコール
    print()

def main():
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


if __name__ == '__main__':
    main()
