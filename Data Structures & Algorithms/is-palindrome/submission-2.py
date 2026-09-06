class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        
        s=s.replace(" ", "")
        s=s.lower()
        right=len(s)-1
        while left<right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:
                    return False
            else:
                if s[left].isalnum()==False:
                    left+=1
                elif s[right].isalnum()==False:
                    right-=1
            
        return True