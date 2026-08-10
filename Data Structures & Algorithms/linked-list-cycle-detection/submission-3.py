# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if head==None:
            return False
        if head.next == None:
            return False

        if head.next.next == None:
            return False

        while fast != None:
            for x in range(2):
                fast = fast.next

                if slow == fast:
                    return True
                if fast.next == None:
                    return False

            slow = slow.next

        return False
