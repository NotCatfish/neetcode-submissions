class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length=len(prices)

        left=0
        right=1
        max_profit=0
        current_profit=0
        while right<length:
            if prices[right]<prices[left]:
                left=right
            else:
                current_profit=prices[right]-prices[left]
                max_profit=max(current_profit,max_profit)

            right+=1
        
        return max_profit