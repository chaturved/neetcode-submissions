class Solution:
    def climbStairs(self, n: int) -> int:
        """
        you can reach ith step 
        from either (i-1)th step of (i-2)th step
        so the number of ways to reach ith step 
        = number of ways to reach (i-1)th step
        + number of ways to reach (i-2)th step
        """

        prev = 1
        curr = 1
        for i in range(2, n + 1):
            curr, prev = prev + curr, curr
        
        return curr