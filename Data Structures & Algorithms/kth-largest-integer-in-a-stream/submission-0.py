import heapq
class KthLargest:
    """
    constructor:
        heapify list
        set k
    add:
        heapq.heappush(h, val)
        for i in range(len(nums))
            pop heap and put item in list
            return kth item
    """

    def __init__(self, k: int, nums: List[int]):
        self.h = [-x for x in nums] 
        heapq.heapify(self.h)
        self.k = k
        self.count = len(nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, -val)
        self.count += 1
        numbers = []
        for i in range(self.count):
            numbers.append(-heapq.heappop(self.h))
        self.h = [-x for x in numbers]
        heapq.heapify(self.h)
        return numbers[self.k - 1]


