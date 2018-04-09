from flask import Flask, render_template, make_response, request, redirect, url_for
import random
import numpy as np
from time import sleep
import time

# flask
app = Flask(__name__)

def count(n):
    start = time.time()
    while n>0:
        n -= 1
    return(time.time() - start)

@app.route('/')
def index():
    title = "ようこそ"
    return render_template('index.html', title=title)

@app.route('/heavy', methods=['GET'])
def heavy():
    start = time.time()
    result = 'hello'
    print('[start] ' + result)

    time.sleep(10)

    elapsed_time = time.time() - start
    print(f'[end] {result} time:{elapsed_time}')
    return(make_response(result))

@app.route('/<string:value>', methods=['GET'])
def light(value):
    start = time.time()
    result = 'hello {0}'.format(value)
    print('[start] ' + result)

    time.sleep(1)

    elapsed_time = time.time() - start
    print(f'[end] {result} time:{elapsed_time}')
    return(make_response(result))

# @app.route("/send1/", methods=['POST'])
# def sendAlert1():
#     # forward_message = count(100000000)
#     start = time.time()
#     sleep(3)
#     forward_message = time.time() - start
#     return render_template('index.html', message=forward_message)


# main
if __name__ == "__main__":
    # 同時アクセスができない（並列処理が不可能）
    # app.run(host='localhost', port=3000)

    # 同時アクセスができる（並列処理が可能）
    app.run(host='localhost', port=3001, threaded=True)
