# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0

        while cur:
            length += 1
            cur = cur.next
        
        if length < 2:
            return None
        
        nth = length - n
        
        if nth == 0:
            return head.next

        prev = None
        cur = head

        for i in range(nth):
            prev = cur
            cur = cur.next
        
        prev.next = cur.next

        return head
