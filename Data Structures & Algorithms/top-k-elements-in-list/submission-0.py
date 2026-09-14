class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        uniq = {i : 0 for i in set(nums)}
        for n in nums:
            uniq[n] += 1
        uniq = dict(sorted(uniq.items(), key = lambda x:x[1]))
        return list(uniq.keys())[-k:]
