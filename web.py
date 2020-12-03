#!/usr/bin/env python
# coding:utf-8
from flask import Flask, request    # Flaskは必須、requestはリクエストパラメータを処理する場合に使用します。
app = Flask(__name__)


# アップロード画像の表示
@app.route('/upload_image')
def upload_image():
    # アップロード画像の表示画面のテンプレートを呼び出し
    return render_template('upload_image.html')

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(host="localhost", port=8080, debug=True)