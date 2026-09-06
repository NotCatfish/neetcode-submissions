class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left=0
        middle=1
        right=2
        lenght=len(nums)
        result=list()

        for left in range(lenght-2):
            while middle<right and right<lenght:
                if nums[left]+nums[middle]+nums[right]==0:
                    if [nums[left],nums[middle],nums[right]] not in result:
                        result.append([nums[left],nums[middle],nums[right]])
                
                right+=1
                middle+=1

        return result