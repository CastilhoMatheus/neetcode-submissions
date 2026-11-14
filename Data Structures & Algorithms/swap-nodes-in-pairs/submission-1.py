# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        prev = dummy
        dummy.next = head

        while prev.next and prev.next.next:
            node1 = prev.next
            node2 = prev.next.next

            prev.next = node2
            node1.next = node2.next
            node2.next = node1

            prev = node1

        return dummy.next


        
        
