from flask import Flask, jsonify
from DataBaseModule import db_call, db_read
from GetContributes import get_contribute_main

app = Flask(__name__)

@app.route('/')
def run_batch():
    try:
        # DBに問い合わせ
        client, collection = db_call()

        if client is not None and collection is not None:
            # クエリでsortされたUser情報格納変数
            document_count, documents = db_read(collection)

            print(f"取得したドキュメントの数は: {document_count}")
            # 同期的スクレイピング実行
            get_contribute_main(documents)

            # DB閉じる
            client.close()

            return jsonify({'message': 'Batch job completed successfully', 'document_count': document_count}), 200

        else:
            return jsonify({'error': 'Failed to connect to database'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
