import model.mysql_connect
import model.util
import model.point as p
import osmnx as ox
import pandas as pd
from shapely.geometry import Point, LineString
from concurrent.futures import ThreadPoolExecutor
import callable.myThread
import copy

table_name_index = "gpsdata"


# 点和速度对应的类
class PointClass(object):
    point = Point

    def __init__(self, point, speed):
        self.point = point
        self.speed = speed


class LineStringClass(object):
    lineString = LineString

    def __init__(self, lineString, name):
        self.lineString = lineString
        self.name = name


# 匹配轨迹信息
def way_handler(data_list):
    data = pd.DataFrame(data_list)
    point_list = []
    for xyz in zip(data['LONGITUDE'], data['LATITUDE'], data['SPEED']):
        if xyz[2] != 0:
            point = Point(xyz[0], xyz[1])
            point_class = PointClass(point, xyz[2])
            point_list.append(point_class)

    roads = p.roads
    # 将所有的坐标点分到不同的路上
    print("开始将坐标点匹配到路上")

    # 拆分成多个集合
    point_splits = model.util.split_list(point_list, 300)
    thread_id = 1
    threads = []

    for point_split in point_splits:
        # 复制对象，用空间换时间，减少多线程导致的资源占用
        roads_copy = copy.copy(roads)
        thread = callable.myThread.myThread(threadID=thread_id, roads=roads_copy, point_list=point_split)
        threads.append(thread)
        thread_id += 1

    for thread in threads:
        thread.start()

    # 等待所有线程执行完毕
    for t in threads:
        t.join()
    print("所有线程执行完毕~")

    # # 保存路名和平均速度
    result = {}
    for th in threads:
        result.update(th.result)
    return result


# 处理请求并响应
def data_handler(request_dict):
    longmin = request_dict['logmin']
    latmix = request_dict['latmin']
    longmax = request_dict['logmax']
    latmax = request_dict['latmax']
    date = request_dict['date']
    hour = request_dict['hour']

    table_index = model.util.get_table_index(date=date)
    table_name = table_name_index + str(table_index['day'])
    # 根据条件获取数据
    data_list = model.mysql_connect.select_data_gpsdata(date=date, table_name=table_name, hour=hour,
                                                        min_longitude=longmin, max_longitude=longmax,
                                                        min_latitude=latmix, max_latitude=latmax)
    print("---- 数据获取完毕 ---- ")
    print(len(data_list))
    return way_handler(data_list)
