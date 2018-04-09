from flask import Flask, render_template, make_response, request, redirect, url_for
import random
import numpy as np
import time

app = Flask(__name__)

# cpu boundな処理
def count(n):
    start = time.time()
    while n>0:
        n -= 1
    return(time.time() - start)


##########
# root
##########
@app.route('/')
def index():
    title = "ようこそ"
    return render_template('index.html', title=title)





##########
# 重い処理
##########
@app.route('/heavy', methods=['GET'])
def heavy():
    start = time.time()
    result = 'heavy'
    print('[start] ' + result)

    count(100000000)

    elapsed_time = time.time() - start
    print(f'[end] {result} time:{elapsed_time}')

    return(make_response(result))





##########
# 軽い処理
##########
@app.route('/<string:value>', methods=['GET'])
def light(value):
    start = time.time()
    print('[start] ' + value)

    count(10000000)

    elapsed_time = time.time() - start
    print(f'[end] {value} time:{elapsed_time}')
    return(make_response(value))






##########
# main
##########
if __name__ == "__main__":
    # 同時アクセスができない（並列処理が不可能）
    # app.run(host='localhost', port=3001)

    # 同時アクセスができる（並列処理が可能）
    app.run(host='localhost', port=3001, threaded=True)
