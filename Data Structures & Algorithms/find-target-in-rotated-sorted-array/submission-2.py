class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def find_min_element_index():
            l, r = 0, n - 1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
            
            return l
        
        def find(l, r):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return -1
        
        min_index = find_min_element_index()
        left = find(0, min_index - 1)
        if left != -1:
            return left

        right =  find(min_index, n - 1)
        if right != -1:
            return right
        
        return -1
        