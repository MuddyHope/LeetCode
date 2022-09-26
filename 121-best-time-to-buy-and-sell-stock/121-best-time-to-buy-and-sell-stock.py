class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if min_val > prices[i]:
                min_val = prices[i]
            elif prices[i] - min_val > max_profit:
                max_profit = prices[i] - min_val
                print(max_profit)
        return max_profit
                
        
                
            
        
        