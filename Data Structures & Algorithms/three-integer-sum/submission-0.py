class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left=0
        lenght=len(nums)
        result=[]

        for left in range(lenght-2):
            if left>0 and nums[left]==nums[left-1]:
                continue
            
            mid=left+1
            right=lenght-1
            while mid<right:
                total=nums[left]+nums[mid]+nums[right]
                if total>0:
                    right-=1
                elif total<0:
                    mid+=1
                else:
                    result.append([nums[left],nums[mid],nums[right]])
                    while mid<right and nums[mid]==nums[mid+1]:
                            mid+=1
                    while mid<right and nums[right]==nums[right-1]:
                            right-=1
                    mid+=1
                    right-=1

        return result