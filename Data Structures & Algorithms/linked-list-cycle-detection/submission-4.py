# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# more efficient solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # As long as fast and fast.next exist, fast can safely jump 2 steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If the fast runner laps the slow runner, there is a cycle!
            if slow == fast:
                return True
                
        # If fast reaches the end (None), there is no cycle
        return False