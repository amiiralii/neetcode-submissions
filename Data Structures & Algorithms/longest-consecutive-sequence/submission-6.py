class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences = defaultdict(int)
        set_nums = set(nums)
        if len(nums) == 0: return 0
        longest = 1
        for num in set_nums:
            if num-1 not in set_nums:
                length = 1
                while num+length in set_nums:
                    length += 1 
                longest = max(length, longest)
        return longest

