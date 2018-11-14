from shapely.geometry import Point, LineString, Polygon
from shapely.geometry import box
from shapely.geometry import MultiPoint, MultiLineString, box


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


# 定义一个路网的全局变量
roads = []
