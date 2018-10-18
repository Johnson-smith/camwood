#!/usr/bin/env python
#coding=utf-8

import time
import datetime
import pytz

#时间戳转换为本地时间(10位)
def timeStampten(num):
    ltime = time.localtime(1479285300)
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S", ltime)
    return timeStr

# 本地时间 转换 为时间戳
dateC1 = datetime.datetime(2015,11,30,15,55,00)
timestamp2 = time.mktime(dateC1.timetuple())
print(timestamp2)
if __name__ == '__main__':
    print(timeStampten(1479285300))





##13位时间戳转换为正常时间
#def timeStamp(timeNum):
#    timeStamp = float(timeNum/1000)
#    timeArray = time.localtime(timeStamp)
#    otherStyleTime = time.strftime("%Y-%m-%d %H:%M", timeArray)
#    print(otherStyleTime)
#timeStamp(143642827511)




