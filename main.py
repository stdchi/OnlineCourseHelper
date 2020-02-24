# -*- coding: utf-8 -*-
'''
@Time    : 2020/2/24 18:23
@Author  : Stdchi
@FileName: main.py
@Software: PyCharm
'''

__author__ = "Stdchi"
__version__ = "1.0.0"


print('\n'.join([''.join([('Love'[(x-y)%4]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))
print(__author__)
print(__version__)
print("请勿用于其他用途，此脚本只用于学习，谢谢！")
from ChaoXing.getCourseInfo import getPartInfo
from ChaoXing.getCourseInfo import getVideoInfo
from ChaoXing.buildData import buildRequset
from ChaoXing.login import getCookies
from Utils.TimeUtils import getTimeStampMilliSecond
import requests
import json

if not input("test now? y/n:\n") == 'y':
    exit("exit")







time_start = getTimeStampMilliSecond()

# 登录太赶就没写了，大家可以自己完善
COOK = getCookies()

# step1 获取章节信息
detail,default = getPartInfo('11643538','201714099','126374609',COOK)

# step2 获取任务信息
task = detail[0] # 测试第一个任务


# if(task['isPassed'] == False):
#     print("任务状态：当前任务未完成")
# else:
#     print("任务状态：当前任务已是完成状态")
#     exit()


# step3 获取视频信息
vData = getVideoInfo(task['objectId'],COOK)
dtime = int(vData['duration'])

# step4 构造参数
params = {
    'reportUrl':default['reportUrl'],
    'token':vData['dtoken'],
    'cId':default['clazzId'],
    'pTime':dtime,
    'dTime':dtime,
    'cTime':'0_{}'.format(dtime),
    'objId':task['objectId'],
    'info':task['otherInfo'],
    'jId':task['jobid'],
    'uId':default['userid']
}

reqData = buildRequset( **params,cookies = COOK)


# 发送请求
res = requests.get(url=reqData['url'],headers =  reqData['headers'])
try:
    res = json.loads(res.text)
    if res['isPassed'] == True:
        print("任务完成")
    else:
        print("任务失败")
except:
    raise Exception("失败")

time_end = getTimeStampMilliSecond()
print("消耗时间:{} 毫秒".format((time_end - time_start)/1000))