class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        hash map plus two pointer sliding window approach
        """

        # seen = {}

        # l = 0
        # r = 0

        # for i in range(len(s1)):
        #     seen[s1[i]] = seen.get(s1[i], 0) + 1

        # while r < len(s2):
        #     while r < len(s2) and seen.get(s2[r], 0) != 0:
        #         seen[s2[r]] -= 1
                
        #         if (r - l + 1) == len(s1):
        #             return True
        #         r += 1

        #     r += 1
        #     l = r
        # return False

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