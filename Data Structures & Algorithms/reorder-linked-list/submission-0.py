# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head

        while fast and fast.next:  
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        prev = slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        h1, h2 = head, prev

        while h2:
            temp1, temp2 = h1.next, h2.next

            h1.next = h2
            h2.next = temp1

            h1, h2 = temp1, temp2

            
