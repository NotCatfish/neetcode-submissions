# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        result=0
        queue=deque([(root,root.val)])

        while queue:
            current_level_len=len(queue)
            for i in range(current_level_len):
                node,max_till_now=queue.popleft()
                if node.val>=max_till_now:
                    result+=1
                new_max=max(max_till_now,node.val)
                if node.left:
                    queue.append((node.left,new_max))
                if node.right:
                    queue.append((node.right,new_max))
        
        return result
