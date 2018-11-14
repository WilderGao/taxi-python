import pymysql


# # 封装的对象
# class car_gps:
#     def __init__(self, taxi_id, longitude, latitude, speed, car_state):
#         self.taxi_id = taxi_id
#         self.longitude = longitude
#         self.latitude = latitude
#         self.speed = speed
#         self.car_state = car_state


# 从第三张表中找出对应时间的数据
def select_data_gpsdata(date, hour, table_name, min_longitude, min_latitude, max_longitude, max_latitude):
    gps_list = []
    db = pymysql.connect(host="10.21.48.11",
                         port=3306,
                         user="root",
                         passwd="123456",
                         db="taxilog",
                         charset="utf8")
    cursor = db.cursor()
    sql = "SELECT ID, LONGITUDE, LATITUDE, SPEED, CAR_STAT1 FROM " + table_name + " WHERE GPS_TIME LIKE '" + date + \
          "%' AND HOUR_REPRE = '" + str(hour) + "' AND LONGITUDE BETWEEN '" + str(min_longitude) + "' AND '" \
          + str(max_longitude) + "' AND LATITUDE BETWEEN '" + str(min_latitude) + "' AND '" + str(max_latitude) + "'"
    print(sql)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        result_dict = {"LONGITUDE": [], "LATITUDE": [], "SPEED": []}

        for row in results:
            longitude = row[1]
            latitude = row[2]
            speed = row[3]
            result_dict['LONGITUDE'].append(longitude)
            result_dict['LATITUDE'].append(latitude)
            result_dict['SPEED'].append(speed)
        return result_dict
    except Exception as e:
        print(e)
        print("ERROR: unable to fetch data")
    finally:
        db.close()
