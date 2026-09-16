class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices) == 1:
        #     return 0
        # if len(prices) == 2:
        #     return max(0, prices[-1] - prices[0])
        # return max( self.maxProfit(prices[:len(prices)//2]),
        #             self.maxProfit(prices[len(prices)//2:]), 
        #             max(prices[len(prices)//2:]) - min(prices[:len(prices)//2]) 
        #         )
        if len(prices) == 1: return 0
        if len(prices) < 3:
            return max(0, prices[-1] - prices[0])
        profit = 0
        left, right = 0, 1
        while right < len(prices):
            if prices[right] - prices[left] > profit:
                profit =  prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right
            right += 1
        return profit
            
            
            
        
        