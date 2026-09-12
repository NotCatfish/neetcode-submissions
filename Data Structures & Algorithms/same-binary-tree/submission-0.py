# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que1=deque([p])
        que2=deque([q])
        val1=[]
        val2=[]

        while que1:
            curr=que1.popleft()
            if curr:
                val1.append(curr.val)
                if curr.left:
                    que1.append(curr.left)
                else:
                    que1.append(None)
                
                if curr.right:
                    que1.append(curr.right)
                else:
                    que1.append(None)
            else:
                val1.append(None)
        
        while que2:
            curr=que2.popleft()
            if curr:
                val2.append(curr.val)
                if curr.left:
                    que2.append(curr.left)
                else:
                    que2.append(None)
                
                if curr.right:
                    que2.append(curr.right)
                else:
                    que2.append(None)
            else:
                val2.append(None)
        if val1==val2:
            return True
        else:
            return False

            