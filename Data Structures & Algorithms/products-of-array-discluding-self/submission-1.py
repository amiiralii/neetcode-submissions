class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        zero_check = []
        for i, k in enumerate(nums): 
            if k == 0: 
                zero_check.append(i)
            else:
                total_prod *= k
        if len(zero_check) > 1:
            return [0]*len(nums)
        if len(zero_check) == 0:
            return [int(total_prod / i) for i in nums]
        final = [0]*len(nums)
        final[zero_check[0]] = total_prod
        return final
            
        