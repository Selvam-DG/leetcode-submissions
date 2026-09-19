class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        result = []
        if n < k:
            return result
        q = deque()

        for r in range(n):
            while q and r - q[0] >= k:
                q.popleft()
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if r >= k-1:
                result.append(nums[q[0]])

        return result