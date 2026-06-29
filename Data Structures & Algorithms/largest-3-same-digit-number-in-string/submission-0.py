class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best_value = -1
        best_str = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                curr = num[i:i+3]
                value = int(curr)
                if best_value < value:
                    best_value = value
                    best_str = curr
        
        return best_str