class TimeMap:

    def __init__(self):
        self.pair = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.pair[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.pair:
            return ""
        
        lst = self.pair[key]
        l, r = 0, len(lst) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if lst[mid][1] <= timestamp:
                res = lst[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res

