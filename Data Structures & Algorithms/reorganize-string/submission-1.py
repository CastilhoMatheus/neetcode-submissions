class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)
        res = ""

        prev = deque()

        while heap or prev:
            if prev and not heap:
                return ""

            count, char = heapq.heappop(heap)
            res += char
            count += 1

            if prev:
                nxt = prev.popleft()
                heapq.heappush(heap, nxt)
            
            if count != 0:
                prev.append((count, char))

        return res