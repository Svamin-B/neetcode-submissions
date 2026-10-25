class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        left and right pointer. right moves forward while storing count of what it visited in hashmap
        if count of that character > 1 then increase l
        keep a running tab on longest length achieved without repeating characters
        """

        l = 0
        r = 0
        highest = 0
        freq = {}

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1
            count = r - l + 1
            highest = max(count, highest)
            r += 1

        return highest
        