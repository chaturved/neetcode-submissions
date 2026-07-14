class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        sum(nums[i...j]) = prefix[j] - prefix[i - 1] = k
        for some fixed j, find if prefix[j] - k = prefix[i - 1] exists in hashmap for i < j
        """

        prefix = {0: 1}
        running_sum = 0
        count = 0
        for j in range(len(nums)):
            running_sum += nums[j]
            count += prefix.get(running_sum - k, 0)
            prefix[running_sum] = prefix.get(running_sum, 0) + 1
        
        return count
        