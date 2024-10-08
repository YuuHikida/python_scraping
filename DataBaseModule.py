import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def read_environmental_variables():
    # .envファイル読み込み(ローカル用)
    load_dotenv()
    # 環境変数から値を読み込み
    username = os.environ.get("NAME")
    password = os.environ.get("PASSWORD")

    # ユーザー名とパスワードをエンコード
    encoded_username = quote_plus(username)
    encoded_password = quote_plus(password)

    # 接続URIを構築
    url_first = os.environ.get("URL_FIRST")
    url_second = os.environ.get("URL_SECOND")

    uri = f"{url_first}{encoded_username}:{encoded_password}{url_second}"

    return uri


def db_call():
    uri = read_environmental_variables()
    # ↓DBサーバーにアクセスしているだけ
    client = MongoClient(uri, server_api=ServerApi('1'))
    # 指定された名前のdbにアクセス
    # 存在しない場合、仮想dbを作成しdataが挿入された時点で物理的なdbが作成される
    db = client['gitInfoContributes']
    # コレクション(テーブル)へのアクセス
    collection = db['user_info']

    try:
        # 以下はadminデータBSに対してping コマンドを使用
        client.admin.command('ping')
        print("-- MongoDB に接続成功 --")
        return client, collection
    except Exception as e:
        print(e)
        # DB close
        client.close()
        return None, None


def db_read(collection):
    # 全てのドキュメントを取得
    documents = collection.find()

    # ドキュメントリスト作成
    docs_list = list(documents)

    # ドキュメントを表示
    for doc in docs_list:
        print(doc)

    # レコード数取得
    documents_count = len(docs_list)

    # 特定の条件でドキュメントを取得
    # query = {"git_name": "YuuHikida"}
    # document = collection.find_one(query)

    print("【DBの値正常読み取れました】")
    return documents_count, docs_list

# CRUD操作 - 作成-
# def db_create(collection):
#     new_document = {
#         "git_name": "TANAKA",
#         "mail": "sekandonoberu@yahoo.co.jp"
#     }
#     another_document = {
#         "git_name": "HIKIDA",
#         "mail": "ponponda0103@gmail.com"
#     }
#
#     insert_result = collection.insert_one(new_document,another_document)
#     print("【dbへの値が正常作成】")
#     print(f"document ID = {insert_result}")
#


# def db_update(collection):
#     # 特定のドキュメントを更新
#     query = {"name": "TANAKA TAROU"}
#     new_values = {"$set": {"name": "HIKIDA YUU"}}
#
#     update_result = collection.update_one(query, new_values)
#     print(f"Matched documents: {update_result.matched_count}")
#     print(f"Modified documents: {update_result.modified_count}")


# def db_delete(collection):
#     # 特定のドキュメントを削除
#     query = {"name": "HIKIDA YUU"}
#     delete_result = collection.delete_one(query)
#     print(f"Deleted documents: {delete_result.deleted_count}")
