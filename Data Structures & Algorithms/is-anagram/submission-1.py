class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) != set(t) or len(s) != len(t):
            return False
        trace = dict()
        for ss,tt in zip(s,t):
            trace[ss] = trace.get(ss,0) + 1
            trace[tt] = trace.get(tt,0) - 1
        for j in trace.values():
            if j!=0: return False
        return True