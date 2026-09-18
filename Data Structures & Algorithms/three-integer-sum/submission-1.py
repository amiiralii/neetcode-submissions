class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def all_two_sum(target, numbers):
            l, r = 0 , len(numbers)-1
            two_sum = []
            while l != r and l < r:
                if numbers[l] + numbers[r] > target:
                    r -= 1
                elif numbers[l] + numbers[r] < target:
                    l += 1
                elif numbers[l] + numbers[r] == target:
                    two_sum.append([numbers[l],numbers[r]])
                    r -= 1
            return two_sum
        
        sort_nums = sorted(nums)
        three_sum = []
        for i in range(len(sort_nums)):
            two_sums = all_two_sum(sort_nums[i] * -1, [sort_nums[j] for j in range(len(sort_nums)) if j != i])
            for ts in two_sums:
                new_triplet = sorted(ts+[sort_nums[i]])
                if new_triplet not in three_sum:
                    three_sum.append(new_triplet)
        return three_sum