class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        r = 0
        max_len = 0

        while r < len(s):
            seen[s[r]] = seen.get(s[r], 0) + 1

            while seen[s[r]] > 1:
                seen[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
