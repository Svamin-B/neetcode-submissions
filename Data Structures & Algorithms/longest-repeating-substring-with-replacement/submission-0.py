class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        start l and r at 0
        keep frequency map
        while l < r
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            if r - l + 1 - max_freq > k
                freq[s[l]] -= 1
                l += 1

            highest = max(r - l + 1, highest)
        return highest
        """

        l = 0
        r = 0
        max_freq = 0
        highest = 0
        freq = {}

        while (l <= r and r < len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])

            if r - l + 1 - max_freq > k:
                freq[s[l]] -= 1
                l += 1

            highest = max(r - l + 1, highest)
            r += 1
        return highest