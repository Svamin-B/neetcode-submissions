class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        use need map to tell what character is needed
        use missing count to tell how many characters are needed
        """
        
        need = {}

        for i in range(len(t)):
            need[t[i]] = need.get(t[i], 0) + 1

        l = 0
        r = 0
        best_len = float('inf')
        best_start = 0
        missing = len(t)

        while r < len(s):

            if s[r] in need:
                if need[s[r]] > 0:
                    missing -= 1
                need[s[r]] -= 1

            while missing == 0:

                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_start = l

                if s[l] in need:
                    need[s[l]] += 1
                    if need[s[l]] > 0:
                        missing += 1
                l += 1
            
            r += 1

        if best_len == float('inf'):
            return ""
        else:
            return s[best_start: best_start + best_len]
            