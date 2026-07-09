class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lenght=len(numbers)
        right=lenght-1
        left=0

        while right>left:
            csum=numbers[left]+numbers[right]
            print(csum)
            if csum==target:
                return [left+1,right+1]
            elif csum>target:
                right-=1
            else:
                left+=1

        