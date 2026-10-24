import heapq
class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        make a heap (-x for x in stones)
        initialize size of heap
        iterate while size > 0
            if size == 1
                pop
                return the element
            pop twice and check:
                if x == y:
                    don't add back any
                    decrease size by 2
                if x < y:
                    add y - x
                    decrease size by 1
                else:
                    add x - y
                    decrease size by 1
        return 0
        """

        h = [-x for x in stones]
        heapq.heapify(h)
        size = len(stones)

        while size > 0:
            if size == 1:
                return -heapq.heappop(h)
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)

            if x == y:
                size = size - 2
            elif x < y:
                heapq.heappush(h, -(y-x))
                size -= 1
            else:
                heapq.heappush(h, -(x-y))
                size -= 1
        return 0
            
