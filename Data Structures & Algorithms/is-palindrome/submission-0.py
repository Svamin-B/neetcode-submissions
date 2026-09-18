class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        s = s.replace(" ", "")
        a = ''.join(reversed(s))

        if s == a:
            return True
        return False 