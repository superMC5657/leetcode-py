# -*- coding: utf-8 -*-
# !@time: 2020-10-11 21:43:08
# !@author: superMC @email: 18758266469@163.com
# !@question title: text-justification

# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。 
# 
#  你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。 
# 
#  要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。 
# 
#  文本的最后一行应为左对齐，且单词之间不插入额外的空格。 
# 
#  说明: 
# 
#  
#  单词是指由非空格字符组成的字符序列。 
#  每个单词的长度大于 0，小于等于 maxWidth。 
#  输入单词数组 words 至少包含一个单词。 
#  
# 
#  示例: 
# 
#  输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#  
# 
#  示例 2: 
# 
#  输入:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# 输出:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
#      因为最后一行应为左对齐，而不是左右两端对齐。
#      第二行同样为左对齐，这是因为这行只包含一个单词。
#  
# 
#  示例 3: 
# 
#  输入:
# words = ["Science","is","what","we","understand","well","enough","to","explain
# ",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# 输出:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
#  
#  Related Topics 字符串 
#  👍 106 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        cur_len, cur_words = 0, []

        for word in words:
            if cur_len + len(word) + len(cur_words) <= maxWidth:
                cur_len += len(word)
                cur_words.append(word)
            else:
                ret.append(self.align(cur_len, cur_words, maxWidth))
                cur_len, cur_words = len(word), [word]

        if len(cur_words) > 0:
            last_line = ""
            for word in cur_words[:-1]:
                last_line += word
                last_line += ' '
            last_line += cur_words[-1]
            last_line += ' ' * (maxWidth - len(last_line))
            ret.append(last_line)

        return ret

    def align(self, cur_len, cur_words, maxWidth):

        num_spaces = maxWidth - cur_len

        if len(cur_words) == 1:
            return cur_words[0] + ' ' * (maxWidth - cur_len)

        this_line = ""
        num_sep, head_sep = divmod(num_spaces, (len(cur_words) - 1))

        for word in cur_words[:-1]:
            this_line += word
            this_line += ' ' * num_sep
            if head_sep >= 1:
                this_line += ' '
                head_sep -= 1
        this_line += cur_words[-1]

        return this_line


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    ret = Solution().fullJustify(words, maxWidth)
    for line in ret:
        print(line)
