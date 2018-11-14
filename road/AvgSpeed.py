import osmnx as ox
import networkx as nx
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import mplleaflet
import numpy as np
import time
from datetime import datetime
from shapely.geometry import Point, LineString, Polygon
from shapely.geometry import box
from shapely.geometry import MultiPoint, MultiLineString, box


class PointClass(object):
    point = 'Point'

    def __init__(self, point, speed):
        self.point = point
        self.speed = speed


# 点和速度对应的类
class PointClass(object):
    point = 'Point'

    def __init__(self, point, speed):
        self.point = point
        self.speed = speed


class LineStringClass(object):
    lineString = 'LineString'

    def __init__(self, lineString, name):
        self.lineString = lineString
        self.name = name


data = pd.read_csv(r'D:\Anaconda\data\result.csv', names=['ID', 'LONGITUDE', 'LATITUDE', 'SPEED', 'CAT_STAT1'],
                   parse_dates=True)
data.head()
