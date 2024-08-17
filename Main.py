import os
import functions_framework
from dotenv import load_dotenv

from DataBaseModule import db_call, db_read, read_environmental_variables
from GetContributes import get_contribute_main


@functions_framework.http
def run_batch(request):
    url = read_environmental_variables()
    if url is None:
        return "error", 500
    return f"成功:{url}"

    # client, collection = db_call()
    #
    # if client is None and collection is None:
    #     # URLが取得できなかった場合、エラーレスポンスを返す
    #     return "Environment variable URL is not set!!!!!.", 500
    # return f"DB読み込み成功"

    #
    # try:
    #     # DBに問い合わせ
    #     client, collection = db_call()
    #
    #     if client is not None and collection is not None:
    #         # クエリでsortされたUser情報格納変数
    #         document_count, documents = db_read(collection)
    #
    #         print(f"取得したドキュメントの数は: {document_count}")
    #         # 同期的スクレイピング実行
    #         get_contribute_main(documents)
    #
    #         # DB閉じる
    #         client.close()
    #
    #         return f"{documents}", 200
    #
    #     else:
    #         return "error: Failed to connect to database", 500
    #
    # except Exception as e:
    #     return f"{e}", 500
