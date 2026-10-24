class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        walk through first string and populate hashmap with character frequency

        walk through second string and decrement hashmap elements
        if any element in hash map is greater than 0, return false
        """
        seen = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1     

        for j in range(len(t)):
            if t[j] in seen:
                seen[t[j]] -= 1
                if seen[t[j]] < 0:
                    return False
            else:
                return False

        for key, vals in seen.items():
            if vals < 0:
                return False
        return True
