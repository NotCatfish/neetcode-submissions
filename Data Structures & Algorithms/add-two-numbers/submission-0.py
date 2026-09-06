# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        
        prev=None

        while curr1!=None:
            next_node=curr1
            curr1.next=prev
            prev=curr1
            curr1=next_node
        
        prev=None
        while curr2!=None:
            next_node=curr2.next
            curr2.next=prev
            prev=curr2
            curr2=next_node
        
        n="".join(str(val) for val in l1)
        m="".join(str(val) for val in l2)
        n=int(n)
        m=int(m)
        result=n+m
        return [int(x) for x in str(result)]
