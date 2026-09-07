class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=0
        maxVal=0
        while right<len(prices):
            currVal=prices[right]-prices[left]
            maxVal=max(currVal,maxVal)
            if prices[right]<prices[left]:
                left=right
            
            right+=1
        return maxVal