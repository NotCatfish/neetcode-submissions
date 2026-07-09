class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1,1,2,8]
        [48,24,6,1]

        lenght=len(nums)

        prefix=[1]*lenght
        postfix=[1]*lenght

        for x in range(1, lenght):
            prefix[x]=prefix[x-1]*nums[x-1]

            postfix[lenght-x-1]=postfix[lenght-x]*nums[lenght-x]


        solution=[1]*lenght
        counter=0
        for x,y in zip(prefix,postfix):
            solution[counter]=x*y
            counter+=1

        return solution

