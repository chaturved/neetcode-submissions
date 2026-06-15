class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        group_by_freq = [[] for _ in range(len(nums) + 1)]
        for num, count in num_freq.items():
            group_by_freq[count].append(num)
        
        most_freq = []
        count = 0
        for i in range(len(nums), 0, -1):
            for num in group_by_freq[i]:
                if len(most_freq) < k:
                    most_freq.append(num)
        
        return most_freq
                