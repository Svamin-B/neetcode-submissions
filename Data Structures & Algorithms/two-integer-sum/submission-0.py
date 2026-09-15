class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0

        while(i < len(nums)):
            need = target - nums[i]
            if(need in seen):
                if(seen[need] != i):
                    return [seen[need], i]
            else:
                seen[nums[i]] = i
            
            i += 1

        