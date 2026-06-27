class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify_max(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush_max(self.heap, val)
        top_k = []
        for _ in range(self.k):
            top_k.append(heapq.heappop_max(self.heap))
        
        k_largest = top_k[-1]
        for num in top_k:
            heapq.heappush_max(self.heap, num)
        
        return k_largest
