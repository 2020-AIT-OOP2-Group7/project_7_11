#!/usr/bin/env python
# coding:utf-8
from flask import Flask, request,render_template,send_from_directory  # Flaskは必須、requestはリクエストパラメータを処理する場合に使用します。
from werkzeug.utils import secure_filename
import glob
import os
app = Flask(__name__)

UPLOAD_FOLDER = './upload_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("index.html")

# アップロード画像の表示
@app.route('/upload_image')
def upload_image():
    files = glob.glob("./upload_images/*")
    urls = []
    for file in files:
        urls.append("/uploaded/" + os.path.basename(file))

    print(urls)
    return render_template("upload_image.html", page_title="アップロードファイル", target_files=urls)

@app.route('/uploaded/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(host="localhost", port=8080, debug=True)