class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        result=0
        left=prices[0]
        right=prices[1]
        for index in range(2,len(prices)):
            if prices[index]<right:
                if prices[index]<left:
                    left=prices[index]
                else:
                    right=prices[index]
            elif prices[index]<left:
                if prices[index]<right:
                    right=prices[index]
                else:
                    left=prices[index]
            
        result=money-left-right
        if result<0:
            return money
        else:
            return result

