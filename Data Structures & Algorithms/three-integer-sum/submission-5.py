from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=set()
        for left in range(len(nums)-2):
            mid=left+1
            right=len(nums)-1

            while mid<right:
                if nums[left]+nums[right]+nums[mid]==0:
                    result.add((nums[left], nums[mid], nums[right]))
                    right-=1
                    mid+=1
                elif nums[left]+nums[right]+nums[mid]<0:
                    mid+=1
                else:
                    right-=1
                
        
        return [list(triplet) for triplet in result]