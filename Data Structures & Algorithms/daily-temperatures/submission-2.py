class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) < 1:
            return []
        lowers = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while lowers and t > lowers[-1][0]:
                greater = lowers.pop()
                res[greater[1]] = i - greater[1]
                if len(lowers) == 0:
                    break
            lowers.append( (t, i) )
        return res
            