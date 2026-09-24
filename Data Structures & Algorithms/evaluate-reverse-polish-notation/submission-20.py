class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calc(stk):
            item = stk.pop()
            if item not in ["+", "-", "*", "/"]:
                return int(item)
            
            right = calc(stk)
            left = calc(stk)

            if item == "+":
                return right + left
            if item == "-":
                return left - right
            if item == "*":
                return right * left
            if item == "/":
                return int( left / right )
        return calc(tokens)