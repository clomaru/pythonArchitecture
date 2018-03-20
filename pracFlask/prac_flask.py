# https://qiita.com/5zm/items/251be97d2800bf67b1c6
# -*- coding: utf-8 -*-
from flask import Flask, render_template, make_response, request, redirect, url_for
import random
import numpy as np
from time import sleep
import time

# flask
app = Flask(__name__)

@app.route('/')
def index():
    title = "ようこそ"
    return render_template('index.html')

# rest api
@app.route('/<string:value>', methods=['GET'])
def hello(value):
    start = time.time()
    result = 'hello {0}'.format(value)
    print('[start] ' + result)

    time.sleep(5)

    elapsed_time = time.time() - start
    print(f'[end] {result} time:{elapsed_time}')
    return(make_response(result))

# main
if __name__ == "__main__":
    # 同時アクセスができない（並列処理が不可能）
    # app.run(host='localhost', port=3000)

    # 同時アクセスができる（並列処理が可能）
    app.run(host='localhost', port=3000, threaded=True)
