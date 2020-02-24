# -*- coding: utf-8 -*-
'''
@Time    : 2020/2/24 18:47
@Author  : Stdchi
@FileName: TimeUtils.py
@Software: PyCharm
'''

import time

def getTimeStampSecond():
    return round(time.time())

def getTimeStampMilliSecond():
    return round(time.time() * 1000)


