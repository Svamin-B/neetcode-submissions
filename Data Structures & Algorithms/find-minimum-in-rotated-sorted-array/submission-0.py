class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        binary search?
        """

        high = len(nums) - 1
        low = 0
        best = nums[high]
        while (low <= high):
            mid = (low + high) // 2

            if best > nums[mid]:
                high = mid
                best = nums[mid]
            else:
                low = mid + 1

        return best