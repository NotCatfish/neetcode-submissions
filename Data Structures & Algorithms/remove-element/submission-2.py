class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        i=0
        end=len(nums)-1
        while i <= end:
            if nums[i]!=val:
                k+=1
                i+=1
            else:
                nums[i]='_'
                nums[i],nums[end]=nums[end],nums[i]
                end-=1
        return k
