class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        coded = ""
        for s in strs:
            if s == "": 
                coded += "ö"
            else: 
                coded += s
                coded += "ñ"
        return coded

    def decode(self, s: str) -> List[str]:
        if len(s) == 0: return []
        original = []
        curr = ""
        for char in s:
            if char == "ö":
                original.append("")
                curr = ""
            elif char == "ñ":
                original.append(curr)
                curr = ""
            else:
                curr += char
        return original

