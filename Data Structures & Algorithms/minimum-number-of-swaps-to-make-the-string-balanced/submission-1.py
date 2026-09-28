class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for char in s:
            if char == "[":
                stack.append(char)
            elif stack:
                stack.pop()
        
        return (len(stack) + 1) // 2




        
