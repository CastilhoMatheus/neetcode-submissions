# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        h1, h2 = list1, list2
        head = ListNode()
        cur = head
        while h1 and h2:

            if h1.val < h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            
            cur = cur.next

        if h1:
            cur.next = h1
        
        if h2:
            cur.next = h2
        
        return head.next


