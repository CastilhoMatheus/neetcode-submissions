class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # list of tuples (timestamp, value) : will always be sorted

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        data = self.store[key]
        
        if len(data) < 1:
            return ""

        L, R = 0, len(data) - 1

        while L <= R:

            mid = L + (R - L) // 2

            if data[mid][0] == timestamp:
                return data[mid][1]
            
            elif data[mid][0] > timestamp:
                R = mid - 1
            
            else:
                L = mid + 1

        return data[R][1] if data[R][0] <= timestamp else ""