class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        str_lst = []

        for i in range(n):
            str_lst.append("1" if nums[i][i] == "0" else "0")

        return "".join(str_lst)