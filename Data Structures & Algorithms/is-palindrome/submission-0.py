class Solution:
    def isPalindrome(self, s: str) -> bool:

        #clean s and keep only alpha or num delete rest and make it single string
        clean_s = ''.join(char.lower() for char in s if char.isalnum())


        #compare front and rear liek a 2pointer return true if same else dfalse
        if clean_s==clean_s[::-1]:
            return True
        else:
            return False