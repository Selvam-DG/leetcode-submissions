class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)

        best = [float('inf')] * n
        answer = float('inf')

        left  = 0
        curr_sum = 0
        min_len = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            
            if curr_sum == target:
                curr_len = right-left+1
            
                if left > 0 and best[left-1] != float('inf'):
                    answer = min(answer, curr_len+best[left-1])

                min_len = min(min_len, curr_len)
            best[right] = min_len

        return -1 if answer == float('inf') else answer