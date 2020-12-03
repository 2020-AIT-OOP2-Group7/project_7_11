#!/usr/bin/env python
# coding:utf-8
from flask import Flask, request,render_template    # Flaskは必須、requestはリクエストパラメータを処理する場合に使用します。
app = Flask(__name__)

# http://127.0.0.1:8080/
@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(host="localhost", port=8080, debug=True)