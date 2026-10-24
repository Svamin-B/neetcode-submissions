class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        walk through array while storing elements in dict
        need = target - nums[i]
        if need in seen, then return [i, seen[need]]
        """
        seen = {}
        need = 0

        i = 0
        while i < len(nums):
            need = target - nums[i]
            
            if need in seen:
                return [seen[need], i]
            seen[nums[i]] = i
            i += 1
            



        