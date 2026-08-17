class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                substr_chars = []
                while stack[-1] != "[":
                    substr_chars.append(stack.pop())
                stack.pop()
                substr_chars.reverse()

                digits = []
                while stack and stack[-1].isdigit():
                    digits.append(stack.pop())
                digits.reverse()
                repeat = int("".join(digits))

                for _ in range(repeat):
                    for c in substr_chars:
                        stack.append(c)
            else:
                stack.append(char)

        return "".join(stack)