class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0 : return True
        start, end = -1, len(s)
        while start < end:
            start += 1
            end -= 1
            while start < end and not ( s[start].isnumeric() or s[start].isalpha()):
                start += 1
            while start < end and not ( s[end].isnumeric() or s[end].isalpha()):
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
        return True