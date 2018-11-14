# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, make_response
from werkzeug.utils import secure_filename
import os
import json

app = Flask(__name__)


@app.route('/paicha/state/judge', methods=['GET', 'POST'])
def state():
    if request.method == 'POST':
        print('已接收到请求/paicha/state/judge')
        a = request.get_data()
        dict1 = json.loads(a)
        print('接受到的Json信息：')
        print(dict1)
        returndict = 0
        returnjson = json.dumps(returndict)
        returnjson = make_response(returnjson)
        returnjson.headers['Access-Control-Allow-Origin'] = '*'
        return returnjson
    else:
        return '只接受post请求！'


@app.route('/paicha/predict/one', methods=['GET', 'POST'])
def predict_one():
    if request.method == 'POST':
        print('已接收到请求/paicha/predict/one')
        a = request.get_data()
        dict1 = json.loads(a)
        print('接受到的Json信息：')
        print(dict1)
        returndict = 0
        print('返回结果')
        print(returndict)
        returnjson = json.dumps(returndict)
        returnjson = make_response(returnjson)
        returnjson.headers['Access-Control-Allow-Origin'] = '*'
        return returnjson
    else:
        return '只接受post请求！'

# 该函数废弃
@app.route('/paicha/guzhang/one', methods=['GET', 'POST'])
def guzhang_one():
    if request.method == 'POST':
        print('已接收到请求/paicha/guzhang/one')
        a = request.get_data()
        dict1 = json.loads(a)
        print('接受到的Json信息：')
        print(dict1)
        returndict = 0
        print('返回结果')
        print(returndict)
        returnjson = json.dumps(returndict)
        returnjson = make_response(returnjson)
        returnjson.headers['Access-Control-Allow-Origin'] = '*'
        return returnjson
    else:
        return '只接受post请求！'


if __name__ =='__main__':
    app.run(host="localhost", port=5050)