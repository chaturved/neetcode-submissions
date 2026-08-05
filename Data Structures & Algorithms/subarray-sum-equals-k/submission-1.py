class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        nums[i..j] = prefix[j] - prefix[i] = k
        so to have a subarray given prefix[j], prefix[j] - k = prefix[i] should be in prefix
        """
        prefix = {0: 1}
        running_sum = 0
        count = 0
        for num in nums:
            running_sum += num
            count += prefix.get(running_sum - k, 0)
            prefix[running_sum] = prefix.get(running_sum, 0) + 1
        
        return count