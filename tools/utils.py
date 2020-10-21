# -*- coding: utf-8 -*-
# !@time: 2020/6/8 01 09
# !@author: superMC @email: 18758266469@163.com
# !@fileName: utils.py
import json


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def prefixAnd(m, n, mat):
    P = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]
    return P


def createtree(Node, l):
    if l[0]:
        root = Node(l[0])
        nodes = [root]
        id = 1
        while nodes and id < len(l):
            node = nodes[0]  # 依次为每个节点分配子节点
            node.left = Node(l[id]) if l[id] else None
            nodes.append(node.left)
            node.right = Node(l[id + 1]) if id < len(l) - 1 and l[id + 1] else None
            nodes.append(node.right)
            id += 2  # 每次取出两个节点
            nodes.pop(0)
        return root
    else:
        return None
