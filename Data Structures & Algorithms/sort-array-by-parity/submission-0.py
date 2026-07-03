class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_lst = []
        odd_lst = []
        for num in nums:
            if num % 2 == 0:
                even_lst.append(num)
            else:
                odd_lst.append(num)
        
        return even_lst + odd_lst