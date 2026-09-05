class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        numcount=0
        onecount=0
        for num in s:
            if int(num)==1:
                onecount+=1
            numcount+=1
        
        if onecount==1:
            return "0"*(numcount-1)+"1"
        else:
            return "1"*(onecount-1)+"0"*(numcount-onecount)+"1"