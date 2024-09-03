# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections


class Solution(object):
    def levelOrder(self, root):
        result = []
        if root == None:
            return result
        queue = collections.deque([root])
        while(queue) :
            level = []
            for _ in range(0,len(queue)): # 这里的len(queue)是因为queue的长度是变化的，不能直接用for cur in queue，但同时不需要先记录queue的长度
                cur = queue.popleft()
                level.append(cur.val)
                if (cur.left):
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result

# key:
"""
1. 先判断空条件
2. 用队列来实现层序遍历
3. 用for _ in range(0,len(queue))来遍历当前层的所有节点
4. 用queue.popleft()来取出当前节点
5. 用queue.append()来添加下一层的节点
6. 用result.append(level)来添加当前层的结果
"""