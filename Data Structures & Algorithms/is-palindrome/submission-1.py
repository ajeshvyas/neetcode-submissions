class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(c.lower() for c in s if c.isalnum())
        rev_s = s[::-1]
        return s == rev_s