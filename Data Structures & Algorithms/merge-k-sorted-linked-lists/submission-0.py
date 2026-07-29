# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[listNode]:
        h1, h2 = l1, l2
        dummy = ListNode()
        cur = dummy
        
        while h1 and h2:
            if h1.val <= h2.val:
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
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def dfs(left, right):
            if left == right:
                return lists[left]
            
            if left > right:
                return

            mid = (left + right) // 2

            l1 = dfs(left, mid)
            l2 = dfs(mid+1, right)

            merged = self.mergeTwoLists(l1, l2)
            return merged

        return dfs(0, len(lists) - 1)