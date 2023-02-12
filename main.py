from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request

from func import *

app = Flask(__name__)

Message = namedtuple('Message', 'text')
messages = []


@app.route('/', methods = ['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/main', methods = ['GET'])
def main():
    return render_template('main.html', messages=messages)

@app.route('/select_file', methods = ['POST'])
def select_file():
    text = request.form['text']
    execute_file(text)
    return redirect(url_for('main'))

@app.route('/find_files', methods = ['POST'])
def find_files():
    option = list_my_progs()
    for i in range(len(option)):
        messages.append(Message(option[i]))
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)