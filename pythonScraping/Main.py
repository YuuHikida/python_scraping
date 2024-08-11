import asyncio

from DataBaseModule import db_call, db_read
from GetContributes import call_contributes


def main():
    # DBに問い合わせ
    client, collection = db_call()
    # クエリでsortされたUser情報格納変数

    if client is not None and collection is not None:
        document_count, documents = db_read(collection)

        print(f"取得したドキュメントの数: {document_count}")
        # 非同期スクレイピング実行
        asyncio.run(call_contributes(documents))
        # DB閉じる
        client.close()


if __name__ == '__main__':
    main()
