"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        storeRandoms = {None: None}
        

        cur = head

        while cur:
            copy = Node(cur.val)
            storeRandoms[cur] = copy
            cur = cur.next
        
        cur = head

        while cur:
            copy = storeRandoms[cur]
            copy.next = storeRandoms[cur.next]
            copy.random = storeRandoms[cur.random]
            cur = cur.next
        
        return storeRandoms[head]

        