class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        k = 0

        while l <= r:
            while l <= r and nums[l] != val:
                l += 1
                k += 1
                
            while l <= r and nums[r] == val:
                r -= 1

            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                k += 1
                r -= 1

        return k