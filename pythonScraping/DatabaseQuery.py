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
    client = MongoClient(uri, server_api=ServerApi('1'))

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


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
