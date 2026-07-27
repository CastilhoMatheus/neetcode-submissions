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
        store_randoms = {None: None} # original -> copy
        cur = head

        while cur:
            newNode = Node(cur.val)
            store_randoms[cur] = newNode

            cur = cur.next
        
        cur = head
        while cur:
            copy = store_randoms[cur]

            copy.next = store_randoms[cur.next]
            copy.random = store_randoms[cur.random]

            cur = cur.next
        
        return store_randoms[head]

            