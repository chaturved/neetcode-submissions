class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = m - 1, n - 1
        zero_pointer = m + n - 1
        while l >= 0 and r >= 0:
            if nums1[l] <= nums2[r]:
                nums1[zero_pointer] = nums2[r]
                r -= 1
            else:
                nums1[zero_pointer] = nums1[l]
                l -= 1
            
            zero_pointer -= 1
        
        while r >= 0:
            nums1[zero_pointer] = nums2[r]
            zero_pointer -= 1
            r -= 1