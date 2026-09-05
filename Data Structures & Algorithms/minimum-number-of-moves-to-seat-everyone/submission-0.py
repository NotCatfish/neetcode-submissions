class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        swap=0
        for index in range(len(seats)):
            if seats[index]!=students[index]:
                swap+=abs(seats[index]-students[index])
        
        return swap