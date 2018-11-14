import threading


class myThread(threading.Thread):
    result = {}
    result_pre = {}

    def __init__(self, threadID, roads, point_list):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.roads = roads
        self.point_list = point_list

    # 线程执行
    def run(self):
        print("线程开始执行，线程Id为", self.threadID)
        self.result = task(point_list=self.point_list, roads=self.roads, result_pre=self.result_pre)
        print("线程", self.threadID, "执行完毕")


def task(point_list, roads, result_pre):
    for point in point_list:
        for road in roads:
            dis = road.lineString.distance(point.point)
            if dis <= 0.01:
                name = road.name
                if name in result_pre.keys():
                    result_pre[name].add(point)
                else:
                    result_pre[name] = set()
                    result_pre[name].add(point)
                continue
    result = {}
    for name, road in result_pre.items():
        s = 0.0
        length = 0
        for point in road:
            # 得到每一条路每一个点的速度
            s += point.speed
            length += 1
        speed = round(s / length, 2)
        result[name] = speed

    return result
