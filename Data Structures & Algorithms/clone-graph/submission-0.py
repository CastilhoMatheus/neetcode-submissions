"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return
        nodes_map = defaultdict()
        nodes_map[node.val] = Node(node.val)

        q = deque([node])

        while q:
            original = deque.popleft(q)

            for nbr in original.neighbors:
                if nbr.val not in nodes_map:
                    nodes_map[nbr.val] = Node(nbr.val)
                    q.append(nbr)
                nodes_map[original.val].neighbors.append(nodes_map[nbr.val])

        
        return nodes_map[node.val]


