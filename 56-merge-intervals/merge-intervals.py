class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        n = len(intervals)
        result =[]
        current = intervals[0]
        for i in range(n):
            if intervals[i][0] <= current[1]:
                current[1] = max(intervals[i][1], current[1])
            else:
                result.append(current)
                current = intervals[i]
        result.append(current)

        return result