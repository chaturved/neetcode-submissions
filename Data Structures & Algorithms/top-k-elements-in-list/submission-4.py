class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = {}
        for num in nums:
            count_nums[num] = count_nums.get(num, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in count_nums.items():
            freq[count].append(num)
        
        result = []
        for i in range(len(freq) - 1, -1, -1):
            while len(freq[i]) > 0 and len(result) < k:
                result.append(freq[i].pop())
        
        return result


