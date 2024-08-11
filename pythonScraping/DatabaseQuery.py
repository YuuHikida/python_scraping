import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def db_call():
    # .envファイルを読み込む
    load_dotenv()
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    # ユーザー名とパスワードをエスケープ
    escaped_username = quote_plus(username)
    escaped_password = quote_plus(password)

    uri = (f"mongodb+srv://{escaped_username}:{escaped_password}@gitinfocontributes.btqfi.mongodb.net/?retryWrites"
           f"=true&w=majority&appName=gitInfoContributes")
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
        print("MongoDB に正常接続")
        db_create(collection)
        print("データの読み取り開始します")
        db_read(collection)
    except Exception as e:
        print(e)


# CRUD操作 - 作成-
def db_create(collection):
    new_document = {
        "name": "TANAKA TAROU",
        "mail": "sekandonoberu@yahoo.co.jp"
    }

    insert_result = collection.insert_one(new_document)
    print("【dbへの値が正常作成】")
    print(f"document ID = {insert_result}")


def db_read(collection):
    # 全てのドキュメントを取得
    documents = collection.find()
    # ドキュメントを表示
    for doc in documents:
        print(doc)
    # 特定の条件でドキュメントを取得
    query = {"name": "John Doe"}
    document = collection.find_one(query)
    print("【DBの値正常読み取れました】")
    print(document)


# import os
# from dotenv import load_dotenv
# from urllib.parse import quote_plus
# from pymongo import MongoClient
#
#
# def db_call():
#     # .envファイルを読み込む
#     load_dotenv()
#     username = os.getenv('USERNAME')
#     password = os.getenv('PASSWORD')
#
#     # ユーザー名とパスワードをエスケープ
#     escaped_username = quote_plus(username)
#     escaped_password = quote_plus(password)
#
#     # 接続文字列を作成
#     connection_url = (f"mongodb+srv://{escaped_username}:{escaped_password}@cluster.mongodb.net/myDatabase?retryWritestrue&w=majority")
#
#     # tls=TrueはMongoDB atlatsheへの接続をTLS(SSL)を有効にするオプション
#     client = MongoClient(connection_url, tls=True)
#     # client = MongoClient(connection_url, tls=True, tlsCertificateKeyFile='/path/to/certificate.pem')
#
#     db = client['testDB']
#     collection = db['testCol']
#     doc_count = collection.count_documents({})
#     print(doc_count)
#
#
