# -*- coding: utf-8 -*-
'''
@Time    : 2020/2/24 19:19
@Author  : Stdchi
@FileName: getCourseInfo.py
@Software: PyCharm
'''
import requests
import json
from Utils.TimeUtils import getTimeStampMilliSecond

# 获取指定章节信息
def getPartInfo(clazzId,courseId,knowledgeid,cookies):
    url = "https://mooc1.chaoxing.com/knowledge/cards?clazzid={}&courseid={}&knowledgeid={}".format(clazzId,courseId,knowledgeid)
    str1 = """try{
    mArg = """
    str2 = """;
}catch(e){"""
    header = {
        'Upgrade-Insecure-Requests':'1',
        'Host': 'mooc1.chaoxing.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Content-Type': 'application/json',
        'Cookie':cookies
    }

    try:
        res = requests.get(url, headers=header)
        res = res.text
        pos1 = str.find(res, str1.encode('utf-8').decode('utf-8'))
        pos2 = str.find(res, str2.encode('utf-8').decode('utf-8'))
        data = json.loads(res[pos1 + len(str1):pos2])
    except:
        raise Exception("## 解析章节信息出错")

    print("==============获取章节信息==============")
    print("该章节内含有 [{}] 段视频".format(len(data['attachments'])))
    for idx,item in enumerate(data['attachments']):
        print("---+ 课程：{}".format(item["property"]["name"]))

    return data['attachments'],data['defaults']


# 获取视频
def getVideoInfo(objectId ,cookies):
    res = None
    try:
        url = "https://mooc1.chaoxing.com/ananas/status/{}?k=&flag=normal&_dc={}".format(objectId,
                                                                                         getTimeStampMilliSecond())
        headers = {
            'Host': 'mooc1.chaoxing.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
            'Cookie': cookies,
            'Referer': 'https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2019-1113-1705',
            'X-Requested-With': 'XMLHttpRequest'
        }
        res = requests.get(url, headers=headers)
        res = json.loads(res.text)
    except:
        raise Exception("## 获取视频信息失败")
    return res

