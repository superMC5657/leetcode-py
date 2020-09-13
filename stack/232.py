# -*- coding: utf-8 -*-
# !@time: 2020-09-10 20:19:17
# !@author: superMC @email: 18758266469@163.com
# !@question title: implement-queue-using-stacks

# 使用栈实现队列的下列操作： 
# 
#  
#  push(x) -- 将一个元素放入队列的尾部。 
#  pop() -- 从队列首部移除元素。 
#  peek() -- 返回队列首部的元素。 
#  empty() -- 返回队列是否为空。 
#  
# 
#  
# 
#  示例: 
# 
#  MyQueue queue = new MyQueue();
# 
# queue.push(1);
# queue.push(2);  
# queue.peek();  // 返回 1
# queue.pop();   // 返回 1
# queue.empty(); // 返回 false 
# 
#  
# 
#  说明: 
# 
#  
#  你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
#  
#  你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。 
#  假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。 
#  
#  Related Topics 栈 设计 
#  👍 223 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []     # 主栈
        self.stack2 = []     # 辅助栈

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        element = self.stack1.pop()
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return element

    def peek(self) -> int:
        """
        Get the front element.
        """
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        element = self.stack1.pop()
        self.stack2.append(element)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        return element

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)

