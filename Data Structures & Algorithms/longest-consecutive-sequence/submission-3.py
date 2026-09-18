class Solution:
   def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}

        i = 0
        while i < len(nums):
            seen[nums[i]] = 1
            i += 1

        max_count = 0

        for key in seen:
            if seen.get(key - 1, 0) == 0:
                count = 1
                check = key

                while seen.get(check + 1, 0) != 0:
                    count += 1
                    check += 1

                max_count = max(max_count, count)

        return max_count

                