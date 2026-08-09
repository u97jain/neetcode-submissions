class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if not self.isAlphaNum(s[left]):
                left += 1
            elif not self.isAlphaNum(s[right]):
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


        
    def isAlphaNum(self, ch):
        return (ord('a') <= ord(ch) <= ord('z') or
                ord('A') <= ord(ch) <= ord('Z') or
                ord('0') <= ord(ch) <= ord('9'))