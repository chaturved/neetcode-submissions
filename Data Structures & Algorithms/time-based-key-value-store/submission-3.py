class TimeMap:

    def __init__(self):
        self.pair = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.pair[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.pair[key]
        if not lst or lst[0][1] > timestamp:
            return ""
        
        l, r = 0, len(lst) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if lst[mid][1] <= timestamp:
                l = mid
            else:
                r = mid - 1
        
        return lst[l][0]