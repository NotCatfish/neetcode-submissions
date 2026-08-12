class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        result=0
        for right in range(len(prices)):
            if prices[left]<prices[right]:
                result=max(result,prices[right]-prices[left])
            else:
                left=right
        
        return result
