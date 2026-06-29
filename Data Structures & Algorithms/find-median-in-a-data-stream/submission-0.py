class MedianFinder:
    def __init__(self):
        self.lower_half = []
        self.upper_half = []

    def addNum(self, num: int) -> None:
        if not self.lower_half or num <= self.lower_half[0]:
            heapq.heappush_max(self.lower_half, num)
            if len(self.lower_half) - len(self.upper_half) > 1:
                value = heapq.heappop_max(self.lower_half)
                heapq.heappush(self.upper_half, value)
            return

        heapq.heappush(self.upper_half, num)
        if len(self.upper_half) - len(self.lower_half) > 1:
            value = heapq.heappop(self.upper_half)
            heapq.heappush_max(self.lower_half, value)
        
    def findMedian(self) -> float:
        if len(self.lower_half) == len(self.upper_half):
            return (self.lower_half[0] + self.upper_half[0]) / 2
        
        if len(self.lower_half) > len(self.upper_half):
            return self.lower_half[0]

        return self.upper_half[0]