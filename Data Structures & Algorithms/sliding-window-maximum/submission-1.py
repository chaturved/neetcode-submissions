class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        brute force: for each moving window compute max and append to output
        time complexity: (n * k)

        for optimal, as window moves left element be removed right element will be addeded
        need to find a way to compute in O(1)?

        heap of size 
        """

        heap = [(nums[i], i) for i in range(k)]
        heapq.heapify_max(heap)

        results = []
        l, r = 0, k - 1
        while r < len(nums):
            results.append(heap[0][0])
            l += 1
            while heap and heap[0][1] < l:
                heapq.heappop_max(heap)
            r += 1
            if r >= len(nums):
                break
            heapq.heappush_max(heap, (nums[r], r))
        
        return results



