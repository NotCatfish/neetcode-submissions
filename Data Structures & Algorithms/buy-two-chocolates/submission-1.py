class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        result=money-prices[0]-prices[1]
        if result<0:
            return money
        else:
            return result