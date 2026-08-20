class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])

        result = []
        n = len(intervals)
        result.append(intervals[0])
        last_seen = result[0]

        for i in range(1, n):
            if intervals[i][0] <= last_seen[1]:
                result[-1][1] = max(intervals[i][1], last_seen[1])
            else:
                last_seen = intervals[i]
                result.append(last_seen)
            
        return result