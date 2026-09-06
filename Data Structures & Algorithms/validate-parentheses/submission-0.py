class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ')': '(', 
            '}': '{', 
            ']': '['
        }
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=bracket_map[s[right]]:
                return False
            left+=1
            right-=1
        return True
            