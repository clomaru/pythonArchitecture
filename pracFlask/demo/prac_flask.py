from flask import Flask, render_template, make_response, request, redirect, url_for
import random
import numpy as np
import pandas as pd
import time

app = Flask(__name__)

# cpu boundな処理
def cpub(n):
    if n < 2:
        return n
    return cpub(n-2) + cpub(n-1)


# I/O boundな処理
def iob():
    big_csv = pd.read_csv('500mb_data.csv')
    return(big_csv.head())


# lightの処理内容
def l1():
    cpub(33)
    print("|-|●|-|l1-1-c end")
    iob()
    print("|-|●|-|l1-2-i end")
    cpub(34)
    print("|-|●|-|l1-3-c end")
    iob()
    print("|-|●|-|l1-4-i end")
    cpub(36)
    print("|-|●|-|l1-5-c end")


# light2の処理内容
def l2():
    iob()
    print("|-|-|●|l2-1-i end")
    cpub(34)
    print("|-|-|●|l2-2-c end")
    iob()
    print("|-|-|●|l2-3-i end")
    cpub(36)
    print("|-|-|●|l2-4-c end")
    iob()
    print("|-|-|●|l2-5-i end")




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
    print('|★|-|-|[start] ' + result)

    cpub(39)

    elapsed_time = time.time() - start
    print(f'|★|-|-|[end] {result} time:{elapsed_time}')

    return(make_response(result))





##########
# 軽い処理 1
##########
@app.route('/light', methods=['GET'])
def light():
    start = time.time()
    result = 'light'
    print('|-|★|-|[start]' + result)

    l1()

    elapsed_time = time.time() - start
    print(f'|-|★|-|[end] {result} time:{elapsed_time}')
    return(make_response(result))


##########
# 軽い処理 2
##########
@app.route('/light2', methods=['GET'])
def light2():
    start = time.time()
    result = 'light2'
    print('|-|-|★|[start]' + result)

    l2()

    elapsed_time = time.time() - start
    print(f'|-|-|★|[end] {result} time:{elapsed_time}')
    return(make_response(result))





##########
# main
##########
if __name__ == "__main__":
    # 同時アクセスができない（並列処理が不可能）
    # app.run(host='localhost', port=3001)

    # 同時アクセスができる（並列処理が可能）
    app.run(host='localhost', port=3001, threaded=True)
