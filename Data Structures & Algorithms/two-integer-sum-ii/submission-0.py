class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        answer = []
        while(l < r):

            if target - (numbers[r] + numbers[l]) > 0:
                l += 1
            elif target - (numbers[r] + numbers[l]) < 0:
                r -= 1
            if target - (numbers[r] + numbers[l]) == 0:
                return [l + 1, r + 1]

        