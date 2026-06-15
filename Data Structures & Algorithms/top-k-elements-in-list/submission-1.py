class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = {}
        for num in nums:
            count_nums[num] = count_nums.get(num, 0) + 1

        max_heap = []
        for key, value in count_nums.items():
            max_heap.append((-value, key))
        
        heapq.heapify(max_heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])
        
        return result
