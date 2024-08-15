import asyncio
from flask import Flask, jsonify, request
from DataBaseModule import db_call, db_read
from GetContributes import get_contribute_main

app = Flask(__name__)


@app.route('/run-batch', methods=['POST'])
def run_batch():
    try:
        # DBに問い合わせ
        client, collection = db_call()

        if client is not None and collection is not None:
            # クエリでsortされたUser情報格納変数
            document_count, documents = db_read(collection)

            print(f"取得したドキュメントの数: {document_count}")

            # 非同期スクレイピング実行
            asyncio.run(get_contribute_main(documents))

            # DB閉じる
            client.close()

            return jsonify({'message': 'Batch job completed successfully', 'document_count': document_count}), 200

        else:
            return jsonify({'error': 'Failed to connect to database'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
