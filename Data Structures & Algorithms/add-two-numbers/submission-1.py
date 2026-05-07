# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ''

        cur = l1

        while cur:
            temp = str(cur.val) + n1 
            n1  = temp
            cur = cur.next

        n2 = ''

        cur = l2

        while cur:
            temp = str(cur.val) + n2 
            n2  = temp
            cur = cur.next
        
        total = int(n1) + int(n2)
        dummy = ListNode()
        prev = dummy
        
        if not total:
            return dummy
        
        while total:         
            rightMost = total % 10
            node = ListNode(rightMost)
            prev.next = node
            prev = node
            total = total // 10
        
        return dummy.next
        
        