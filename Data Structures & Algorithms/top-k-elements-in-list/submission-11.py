class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            bucket[count].append(num)
        
        count = 0
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                count += 1
                if count == k:
                    return res
