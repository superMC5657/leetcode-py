# -*- coding: utf-8 -*-
# !@time: 2020/8/31 12:19 上午
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 3.py

U = {"1": "abc", "2": "dba", "3": "bed"}


def sort_dict(U):
    U_set = dict()
    for key, value in U.items():
        U_set[key] = set(value)
    return U_set


U_set = sort_dict(U)
print(U_set)

x = 'abde'
x = set(x)
"""
因为x和 U里的值都是unique的 不重复的 所以用set做交集最好
"""
max_match_num = 0
cache_key_list = list()
for key, value in U_set.items():
    match_num = len(x & value)
    if max_match_num < match_num:
        cache_key_list = [key]
        max_match_num = match_num
    elif max_match_num == match_num:
        cache_key_list.append(key)

for cache_key in cache_key_list:
    print(cache_key + U[cache_key])
