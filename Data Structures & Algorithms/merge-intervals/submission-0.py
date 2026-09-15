class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort elements
        for each element, assign min and max.
            for each next element, if max is less than new_el[1] and greater than new_el[0]. Max is new_el[1]. Else break
        """

        intervals.sort()
        answer = []
        i = 0
        while i < len(intervals):
            least = intervals[i][0]
            most = intervals[i][1]
            j = i + 1
            while j < len(intervals) and intervals[j][0] <= most:
                most = max(most, intervals[j][1])
                j += 1
        
            answer.append([least, most])
            i = j
        return answer
        
