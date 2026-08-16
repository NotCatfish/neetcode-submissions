import random
def random_qsort(arr):
    if len(arr)<=1:
        return arr
    pivot=random.choice(arr)

    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]

    return random_qsort(left)+middle+random_qsort(right)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return random_qsort(nums)