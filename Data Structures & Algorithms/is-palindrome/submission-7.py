class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        new_s = []
        for j in range(len(s)):
            if s[j].isnumeric() or s[j].isalpha():
                new_s += s[j]
        if len(new_s)==0 : return True
        start, end = -1, len(new_s)
        while start < end:
            start += 1
            end -= 1
            if new_s[start] != new_s[end]:
                return False
        return True