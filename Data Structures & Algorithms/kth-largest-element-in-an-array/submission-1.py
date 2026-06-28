class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l, r):
            pivot = nums[r]
            store = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[store] = nums[store], nums[i]
                    store += 1
            
            nums[store], nums[r] = nums[r], nums[store]
            return store
        
        l, r = 0, len(nums) - 1
        target = len(nums) - k
        pivot = -1
        while pivot != target:
            pivot = partition(l, r)
            if pivot < target:
                l = pivot + 1
            else:
                r = pivot - 1
        
        return nums[target]
                