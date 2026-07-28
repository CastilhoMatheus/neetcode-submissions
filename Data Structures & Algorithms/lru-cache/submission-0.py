class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)

        self.left.next, self.right.prev = self.right, self.left # [0, 0] <=> [0,0]

    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.add(self.cache[key])

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            last = self.left.next
            self.delete(last)
            del self.cache[last.key]

    def add(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node
    
    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev