# -*- coding: utf-8 -*-
'''
@Time    : 2020/2/24 18:29
@Author  : Stdchi
@FileName: QuickStudy.py
@Software: PyCharm
'''

from Utils.EncodeUtils import md5
from Utils.TimeUtils import getTimeStampMilliSecond

def buildRequset(reportUrl,token,cId,pTime,dTime,cTime,objId,info,jId,uId,cookies):
    isdrag = '0'
    enc = getEnc(cId, pTime, dTime, cTime, objId, jId, uId)
    rt = '0.9'
    timestamp = getTimeStampMilliSecond()
    url = "{}/{}?clazzId={}&playingTime={}&duration={}&clipTime={}&objectId={}&otherInfo={}&jobid={}&userid={}&isdrag={}&view=pc&enc={}&rt={}&dtype=Video&_t={}".format(
        reportUrl,
        token,
        cId,
        pTime,
        dTime,
        cTime,
        objId,
        info,
        jId,
        uId,
        isdrag,
        enc,
        rt,
        timestamp
    )

    header = {
        'Host':'mooc1.chaoxing.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Content-Type':'application/json',
        'Referer':'https://mooc1.chaoxing.com/ananas/modules/video/index.html?v=2019-1113-1705',
        'Cookie':cookies
    }
    data = {
        'url':url,
        'headers' : header
    }
    return data


def getEnc(cId, pTime, dTime, cTime, objId, jId, uId):
    str = "[{0}][{1}][{2}][{3}][{4}][{5}][{6}][{7}]".format(
        cId,uId,jId,objId,int(pTime) * 1000, 'd_yHJ!$pdA~5',int(dTime) * 1000,cTime
    )
    return md5(str)

