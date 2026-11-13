class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)

        dq = deque()
        right = n - 1
        cost = 0
        ans = 0

        for left in range(n - 1, -1, -1):

            # Add nums[left] to the window
            while dq and nums[dq[-1]] < nums[left]:
                idx = dq.pop()

                end = dq[-1] if dq else right + 1

                cost += (end - idx) * (nums[left] - nums[idx])

            dq.append(left)

            # Shrink window until cost <= k
            while cost > k:
                cost -= nums[dq[0]] - nums[right]

                if dq[0] == right:
                    dq.popleft()

                right -= 1

            # Count all valid subarrays starting at left
            ans += right - left + 1

        return ans