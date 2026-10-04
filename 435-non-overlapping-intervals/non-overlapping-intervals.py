class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        lastEnd = float('-inf')
        removeCount = 0

        for interval in intervals:
            if interval[0]>= lastEnd:
                lastEnd = interval[1]
            
            else:
                removeCount += 1
            
        return removeCount