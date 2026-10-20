class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        def can_sort(k):
            prev_max = float('-inf')

            for start in range(0, n, k):
                end = start + k

                # Check whether this block is a rotated sorted array.
                descents = 0
                block_min = float('inf')
                block_max = float('-inf')

                for i in range(start, end):
                    x = nums[i]
                    block_min = min(block_min, x)
                    block_max = max(block_max, x)

                    nxt = nums[start] if i == end - 1 else nums[i + 1]
                    if x > nxt:
                        descents += 1
                        if descents > 1:
                            return False

                # Previous block must not contain larger elements.
                if prev_max > block_min:
                    return False

                prev_max = block_max

            return True

        ans = 0

        # Only divisors of n can be sortable.
        for k in range(1, int(n ** 0.5) + 1):
            if n % k == 0:
                if can_sort(k):
                    ans += k

                other = n // k
                if other != k and can_sort(other):
                    ans += other

        return ans
