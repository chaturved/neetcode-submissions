class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1], x[2], x[0]))
        heap = []
        curr = 0
        for passengers, start, end in trips:
            while heap and heap[0][0] <= start:
                _, carrying = heapq.heappop(heap)
                curr -= carrying
            
            curr += passengers
            if curr > capacity:
                return False

            heapq.heappush(heap, (end, curr))
        
        return True
        