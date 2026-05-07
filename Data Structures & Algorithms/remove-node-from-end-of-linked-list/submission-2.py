# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:     
        size = 0
        cur = head

        while cur:
            size += 1
            cur = cur.next
       
        i = size - n
        if i == 0:
            return head.next
        
        cur = head
        for j in range(size - 1):
            if (j + 1) == i:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head