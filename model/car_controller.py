from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_cors import *
import json
import model.car_handler
import osmnx as ox
import model.point

app = Flask(__name__)
CORS(app)


@app.route('/trajectory', methods=['GET', 'POST'])
def state():
    if request.method == 'POST':
        print('已接收到请求/paicha/state/judge')
        a = request.get_data()
        # 将json转化为对象
        dict1 = json.loads(a)
        print(dict1)
        return_dict = model.car_handler.data_handler(dict1)
        return_json = json.dumps(return_dict)
        return_json = make_response(return_json)
        return_json.headers['Access-Control-Allow-Origin'] = '*'
        return return_json
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


if __name__ == '__main__':

    # 获取路网信息
    print("开始路网匹配")
    huangpu = ox.graph_from_file("D:\Anaconda\data\huangpu\huangpu.osm", network_type="drive")
    nodes, edges = ox.graph_to_gdfs(huangpu)
    edges["name"].fillna("nan", inplace=True)


    def list_perform(x):
        if type(x) == type([]):
            return x[0]
        else:
            return x


    edges['name'] = edges['name'].apply(lambda x: list_perform(x))
    huangpu_edges = edges
    huangpu_edges = huangpu_edges[huangpu_edges['name'] != "nan"]

    # 将道路的轨迹和路名对应起来
    roads = []
    for xy in zip(huangpu_edges['geometry'], huangpu_edges['name']):
        road = model.point.LineStringClass(xy[0], xy[1])
        roads.append(road)
    model.point.roads = roads

    app.run(host="192.168.1.110", port=5050)
