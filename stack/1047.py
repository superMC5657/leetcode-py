# -*- coding: utf-8 -*-
# !@time: 2021-03-09 01:16:49	
# !@author: superMC @email: 18758266469@163.com
# !@fileName: remove-all-adjacent-duplicates-in-string.py

# 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。 
# 
#  在 S 上反复执行重复项删除操作，直到无法继续删除。 
# 
#  在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。 
# 
#  
# 
#  示例： 
# 
#  输入："abbaca"
# 输出："ca"
# 解释：
# 例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又
# 只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= S.length <= 20000 
#  S 仅由小写英文字母组成。 
#  
#  Related Topics 栈 
#  👍 126 👎 0



# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stk = list()
        for ch in S:
            if stk and stk[-1] == ch:
                stk.pop()
            else:
                stk.append(ch)
        return "".join(stk)
# leetcode submit region end(Prohibit modification and deletion)
