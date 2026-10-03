class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min_heap = [] # will contain top 2 max elements
        max_heap = [] # will contain top 2 min elements

        for num in nums:
            heapq.heappush(min_heap, num)
            heapq.heappush_max(max_heap, num)

            if len(min_heap) > 2:
                heapq.heappop(min_heap)

            if len(max_heap) > 2:
                heapq.heappop_max(max_heap)
        
        ab_product = heapq.heappop(min_heap) * heapq.heappop(min_heap)
        cd_product = heapq.heappop_max(max_heap) * heapq.heappop_max(max_heap)
        return ab_product - cd_product