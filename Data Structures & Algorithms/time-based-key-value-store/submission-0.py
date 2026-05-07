class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
            self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        res, array = "", self.store[key]

        l, r = 0, len(array) - 1

        while l <= r:
            mid = (r + l) // 2

            if array[mid][1] <= timestamp:
                res = array[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res
        