class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                right = stack.pop()
                left = stack.pop()

                if i == "+":
                    res = right + left
                if i == "-":
                    res = left - right
                if i == "*":
                    res = right * left
                if i == "/":
                    res = int( left / right )
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[-1]
