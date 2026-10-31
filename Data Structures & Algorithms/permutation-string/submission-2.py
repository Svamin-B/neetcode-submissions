class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        hash map plus two pointer sliding window approach
        """
        l = 0
        r = l + len(s1)
        sorted1 = sorted(s1)
        while r <= len(s2):
            if sorted1 == sorted(s2[l:r]):
                return True
            else:
                l += 1
                r += 1
        return False