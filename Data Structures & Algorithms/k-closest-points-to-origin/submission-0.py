import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        points = [[1,2], [2,4]]
        walk through points and:
            calculate distances of each element in points and store in list of tuples (distance, [x,y])
        make min heap of distances list of tuples
        pop k times
        append each answer to answer list
        """
        distances = []
        for i in range(len(points)):
            distance = math.sqrt((points[i][0] - 0)**2 + (points[i][1] - 0)**2)
            distances.append((distance, points[i]))
            
        heapq.heapify(distances)
        count = 0
        answer = []
        while count < k:
            answer.append(heapq.heappop(distances)[1])
            count += 1

        return answer

        


