class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_kth(a, b, k, i=0, j=0):
            if len(a) - i > len(b) - j:
                return get_kth(b, a, k, j, i)
            if i == len(a):
                return b[j + k - 1]
            if k == 1:
                return min(a[i], b[j])

            m, n = len(a) - i, len(b) - j
            ai = min(m, k // 2)
            bj = min(n, k // 2)

            if a[i + ai - 1] <= b[j + bj - 1]:
                return get_kth(a, b, k - ai, i + ai, j)
            return get_kth(a, b, k - bj, i, j + bj)

        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return get_kth(nums1, nums2, (total + 1) // 2)
        return (get_kth(nums1, nums2, total // 2) + get_kth(nums1, nums2, total // 2 + 1)) / 2