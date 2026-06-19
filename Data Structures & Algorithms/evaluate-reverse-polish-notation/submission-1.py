class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        for token in tokens:
            if token in operations:
                right = stack.pop()
                left = stack.pop()
                match token:
                    case "+":
                        stack.append(left + right)
                    case "-":
                        stack.append(left - right)
                    case "*":
                        stack.append(left * right)
                    case "/":
                        stack.append(int(left / right))
            else:
                stack.append(int(token))
        
        return stack.pop()
