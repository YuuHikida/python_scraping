from DataBaseModule import db_call, db_read
from GetContributes import call_contributes


def main():
    # DBに問い合わせ
    client, collection = db_call()
    if client is not None and collection is not None:
        db_read(collection)
        # DB閉じる
        client.close()


if __name__ == '__main__':
    main()
