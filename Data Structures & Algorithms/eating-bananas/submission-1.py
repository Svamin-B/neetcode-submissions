class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        h = total allowable eating hours
        k = bananas per hour (if piles[i] < k, piles[i] = 0)
        find the min k such that all piles[i] = 0 within h hours

        binary search on k
        for each mid value, we must go through piles and remove k if piles[i] > k. If piles[i] is less than k after subtracting, piles[i]= 0. Every time k is removed, increment hour count
        """

        l = 1
        r = max(piles)

        while (l <= r):
            mid = (l + r) // 2
            count = 0

            for i in range(len(piles)):
                remaining = piles[i]
                if remaining <= mid:
                    count += 1
                else:
                    count += (remaining + mid - 1) // mid   
            
            if count <= h:
                r = mid - 1
            elif count > h:
                l = mid + 1

        return l
            