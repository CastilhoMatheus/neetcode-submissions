class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)
        res = ""

        prev = None

        while heap or prev:
            if prev and not heap:
                return ""

            count, char = heapq.heappop(heap)
            res += char
            count += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None
            
            if count != 0:
                prev = (count, char)

        return res