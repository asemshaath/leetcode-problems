class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        pointer = 0
        bestProfit = 0
        
        for i in range(1, len(prices)):
            
            if prices[i] - prices[pointer] > bestProfit:
                bestProfit = prices[i] - prices[pointer]
            elif prices[i] - prices[pointer] <= 0:
                pointer = i
            
                
                
        return bestProfit
