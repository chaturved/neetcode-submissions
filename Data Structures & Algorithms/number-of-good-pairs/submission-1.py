class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        pairs = 0
        print(freq)
        for count in freq.values():
                pairs += count * (count - 1) // 2

        return pairs