class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) < 1:
            return []
        lowers = [(temperatures[0],0)]
        res = [ 0 for i in range(len(temperatures))]
        for i, t in enumerate(temperatures):
            while t > lowers[-1][0]:
                greater = lowers.pop()
                res[greater[1]] = i - greater[1]
                if len(lowers) == 0:
                    break
            if i!= 0:
                lowers.append( (t, i) )
        return res
            