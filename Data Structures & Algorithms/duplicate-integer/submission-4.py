class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Returns true if element repeated. Keep a hashmap of         previous entries?

        walk through array. check if element is in the hashmap. If yes return true. If all elements checked, return false
        """

        seen = set()

        for i in range(len(nums)):

            if nums[i] in seen:
                return True

            seen.add(nums[i])
        return False