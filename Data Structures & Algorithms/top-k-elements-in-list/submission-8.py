class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        freq_bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            freq_bucket[count].append(num)
        
        result = []
        for i in range(len(nums), 0, -1):
            for num in freq_bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
