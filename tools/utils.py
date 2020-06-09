# -*- coding: utf-8 -*-
# !@time: 2020/6/8 01 09
# !@author: superMC @email: 18758266469@163.com
# !@fileName: utils.py
import json

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])
