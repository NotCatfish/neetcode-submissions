class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)
        cleaned=cleaned.lower()
        if cleaned==cleaned[::-1]:
            return True
        else:
            return False
