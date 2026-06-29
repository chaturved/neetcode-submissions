class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(brackets, open_count=0, close_count=0):
            if open_count == n and close_count == n:
                result.append("".join(brackets))
                return
                
            if open_count < n:
                brackets.append("(")
                backtrack(brackets, open_count + 1, close_count)
                brackets.pop()
            
            if open_count > close_count:
                brackets.append(")")
                backtrack(brackets, open_count, close_count + 1)
                brackets.pop()
        
        backtrack([])
        return result

            
