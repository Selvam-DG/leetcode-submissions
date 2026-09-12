class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        arr = [(l,r,w,idx) for idx, (l,r,w) in enumerate(intervals)]

        arr.sort()
        n = len(arr)

        start = [x[0] for x in arr]
        next_idx = [0] * n

        for i in range(n):
            next_idx[i] = bisect_right(start, arr[i][1])

        
        @cache
        def dfs(i, remaining):
            if i == n or remaining == 0:
                return 0, ()
            
            # skip
            skip_weight, skip_indices = dfs(i+1, remaining)

            # take
            _, _, weight, original_idx = arr[i]

            next_weight, next_indices = dfs(next_idx[i], remaining-1)


            take_weight = weight + next_weight
            take_indices = tuple(sorted((original_idx, ) + next_indices))

            if take_weight > skip_weight:
                return take_weight, take_indices
            
            if take_weight < skip_weight:
                return skip_weight, skip_indices
            
            return take_weight, min(take_indices, skip_indices)
        
        _, ans = dfs(0,4)

        return list(ans)