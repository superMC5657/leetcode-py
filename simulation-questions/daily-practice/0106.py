# -*- coding: utf-8 -*-
# !@time: 2020/8/31 12:42 上午
# !@author: superMC @email: 18758266469@163.com
# !@fileName: 0106.py

"""
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，
则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。
"""


class Solution:
    def compressString(self, S: str) -> str:
        if S == '':
            return ''
        new_S = ''
        chr_cache = ''
        len_cache = 1
        for chr in S:
            if chr_cache == '':
                chr_cache = chr
                new_S += chr
                continue
            if chr == chr_cache:
                len_cache += 1
            else:
                new_S += str(len_cache)
                len_cache = 1
                new_S += chr
                chr_cache = chr
        new_S += str(len_cache)
        if len(new_S) >= len(S):
            return S
        return new_S


if __name__ == '__main__':
    new_S = Solution().compressString("bb")
    print(new_S)
