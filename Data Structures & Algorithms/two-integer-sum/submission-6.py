class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = []
        for i, n in enumerate(nums):
            new_list.append( (i, n) )
        new_list = sorted(new_list, key = lambda x:x[1] )
        
        left, right = 0, len(new_list) - 1

        while left < right:
            if  new_list[left][1] + new_list[right][1] == target:
                return [min(new_list[left][0], new_list[right][0]), 
                        max(new_list[left][0], new_list[right][0])]
            if  new_list[left][1] + new_list[right][1] > target:
                right -= 1
            if  new_list[left][1] + new_list[right][1] < target:
                left += 1
        
        return []