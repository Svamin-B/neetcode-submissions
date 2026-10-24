class Solution:
   def longestConsecutive(self, nums: List[int]) -> int:
        """
        walk through nums
        if current element - 1 is in set, start searching ahead with count of 2
        on each iteration, check with max and update accordingly
        return max
        """
        numbers = set(nums)
        highest = 0

        for num in numbers:
            # only start if this is the beginning of a sequence
            if num - 1 not in numbers:
                count = 1
                while num + count in numbers:
                    count += 1
                highest = max(highest, count)

        return highest


                