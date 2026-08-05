class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedList=[]
        for position,speed in zip(position,speed):
            sortedList.append((position,speed,(target-position)/speed))
        
        sortedList.sort()
        fleets=0
        etatop=0
        #pop top element and store its eta 
        for x in range(len(sortedList)):
        #compare the eta of top element and if etatop>etanext fleets stays same
            if etatop:
                _,_,etanext=sortedList.pop()
                #if etatop<etanext fleets+=1 and etatop=etanext
                if etatop<etanext:
                    fleets+=1
                    etatop=etanext
                    #repeat above 2 till stack empty
            else:
                _,_,etatop=sortedList.pop()
                fleets+=1

        return fleets
                
            
