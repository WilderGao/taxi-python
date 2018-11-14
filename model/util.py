import model.mysql_connect
import datetime
import time


def get_table_index(date):
    date_time = datetime.datetime.strptime(date, "%Y-%m-%d")
    # 分别获得日期和月份
    day = date_time.strftime("%d")
    month = date_time.strftime("%m")
    if month == 3:
        day += 28
    date_result = {'month': month, 'day': int(day)}
    return date_result


# 把一个集合拆分成多个集合，arr为原始集合，n为集合的个数

def split_list(arr, n):
    return [arr[i:i + n] for i in range(0, len(arr), n)]

