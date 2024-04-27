class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = float ('inf')
        maxProfit = 0

        for i in prices:
            if minVal > i:
                minVal = i
            elif i - minVal > maxProfit:
                maxProfit = i - minVal

        return maxProfit
        
