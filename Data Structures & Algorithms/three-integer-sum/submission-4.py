from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result=list(list())
        length=len(nums)

        for left in range(0,length-2):
            mid=left+1
            right=length-1
            if left==0 or nums[left]!=nums[left-1]:
                while mid<right:
                    addition=nums[left]+nums[mid]+nums[right]
                    if addition==0:
                        if [nums[left],nums[mid],nums[right]] not in result:
                            result.append([nums[left],nums[mid],nums[right]])

                        mid+=1
                        right-=1
                    elif addition<0:
                        mid+=1
                    else:
                        right-=1
            
                
        return result