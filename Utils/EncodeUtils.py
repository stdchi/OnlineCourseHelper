# -*- coding: utf-8 -*-
'''
@Time    : 2020/2/24 18:50
@Author  : Stdchi
@FileName: EncodeUtils.py
@Software: PyCharm
'''

import hashlib


def md5(data):
    return str.lower(hashlib.md5(data.encode(encoding='UTF-8')).hexdigest())