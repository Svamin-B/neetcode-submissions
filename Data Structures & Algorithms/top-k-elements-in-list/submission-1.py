import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        walk through nums
        store num and count in hashmap
        turn hashmap into max heap
        pop from max heap k times
        append popped element to answer
        """
        h = []
        counts = {}
        answer = []
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1

        for key, val in counts.items():
            heapq.heappush(h, (-val,key))

        j = 0 
        while j < k:
            next = heapq.heappop(h)
            answer.append(next[1])
            j += 1

        return answer
        
