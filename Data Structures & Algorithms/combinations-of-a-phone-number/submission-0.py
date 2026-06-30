class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = []
        length = len(digits)

        if length == 0:
            return result

        def backtrack(char_lst, i):
            if i == length:
                result.append("".join(char_lst))
                return

            for char in digit_letters[digits[i]]:
                char_lst.append(char)
                backtrack(char_lst, i + 1)
                char_lst.pop()
        
        backtrack([], 0)
        return result



