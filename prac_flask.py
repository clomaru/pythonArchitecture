from flask import Flask, render_template, request, redirect, url_for
import random
import numpy as np
from time import sleep
import time

app = Flask(__name__)


@app.route('/')
def index():

    title = "ようこそ"
    return render_template('index.html', title=title)


@app.route('/post', methods=['GET', 'POST'])
def post():

    title = "こんにちは"
    if request.method == 'POST':
        start = time.time()
        name = request.form['name']
        sleep(5)
        elapsed_time = time.time() - start

        return render_template('index.html', name=name, title=title, elapsed_time=elapsed_time)

    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
