# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        cur = head
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        prev = None
        i = k

        while cur and i:
            prev = cur
            cur = cur.next
            i -= 1

        if i != 0:
            return head

        prev.next = None
        new_head = self.reverse(head)
        head.next = self.reverseKGroup(cur, k)
        return new_head