class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_keys = {")" : "(", "]" : "[", "}" : "{"}
        if len(s) % 2 == 1:
            return False
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if len(stack) == 0 or stack[-1] != char_keys[char]:
                    return False
                else:
                    stack = stack[:-1]
        return True if len(stack) == 0 else False