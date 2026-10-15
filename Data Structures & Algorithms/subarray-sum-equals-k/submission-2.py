class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        nums[i..j] = prefix[j] - prefix[i - 1] = k
        as looping from j we can check if prefix[j] - k exists 
        if yes then occurences of prefix[] is number of ways
        sum all of them 

        """

        prefix = defaultdict(int)
        prefix[0] = 1
        ways = 0
        curr_sum = 0
        for j in range(len(nums)):
            curr_sum += nums[j]
            if curr_sum - k in prefix:
                ways += prefix[curr_sum - k]
            prefix[curr_sum] += 1 
        
        return ways
