class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length=len(prices)

        left=0
        right=length-1
        max_profit=0
        while left<right:
            if prices[left]>prices[right]:
                left+=1
            else:
                current_profit=prices[right]-prices[left]
                max_profit=max(current_profit,max_profit)
                right-=1

        return max_profit