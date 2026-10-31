class Solution:
    def trap(self, height: List[int]) -> int:
        """
        keep a running tab of left and right max
        use two pointer approach, l = 0, r = len(height) - 1
        if height[l] <= height[r]:
            add water from left
        otherwise right
        """

        l = 0
        r = len(height) - 1
        left_max = 0
        right_max = 0
        total = 0

        while l < r:
            if height[l] <= height[r]:
                left_max = max(left_max, height[l])
                total += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                total += right_max - height[r]
                r -= 1
        return total

        
            


