
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        # Find the smallest maximum difference
        # achievable using at most k operations.
        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        threshold = left

        # Reduce every difference above threshold.
        remaining = k
        answer = 0

        for d in diff:
            if d > threshold:
                remaining -= d - threshold
                d = threshold
            answer += d * d

        # Use remaining operations to reduce
        # differences equal to threshold by 1.
        answer -= remaining * (2 * threshold - 1)

        return answer
