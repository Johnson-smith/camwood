#!/usr/bin/env python
#coding=utf-8

import time
import datetime
import pytz

#时间戳转换为本地时间(10位)
def timeStampten(num):
    ltime = time.localtime(num)
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S", ltime)
    return timeStr
print(timeStampten(1479285300))

##时间戳转换为本地时间（13位）
def timeStamp(timeNum):
    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M", timeArray)
    print(otherStyleTime)
print(timeStamp(1436428275113))
	
	
# 本地时间 转换 为时间戳
dateC1 = datetime.datetime(2015,11,30,15,55,00)
timestamp2 = time.mktime(dateC1.timetuple())
print(timestamp2)


## utc时间转换为时间戳
def utc_to_local(utc_time_str, utc_format='%Y-%m-%dT%H:%MZ'):
    local_tz = pytz.timezone('Asia/Chongqing')
    local_format = "%Y-%m-%d %H:%M"
    utc_dt = datetime.datetime.strptime(utc_time_str, utc_format)
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    time_str = local_dt.strftime(local_format)
    return int(time.mktime(time.strptime(time_str, local_format)))
print(utc_to_local('2018-11-24T16:00Z'))

### utc转换成本地时间
print(time.strftime("%Y-%m-%d %H:%M", time.localtime(utc_to_local('2018-11-24T16:00Z'))))



## 时间戳转换为UTC
def local_to_utc(local_ts, utc_format='%Y-%m-%dT%H:%MZ'):
    local_tz = pytz.timezone('Asia/Chongqing')
    local_format = "%Y-%m-%d %H:%M"
    time_str = time.strftime(local_format, time.localtime(local_ts))
    dt = datetime.datetime.strptime(time_str, local_format)
    local_dt = local_tz.localize(dt, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt.strftime(utc_format)
local_to_utc(1479285300)








