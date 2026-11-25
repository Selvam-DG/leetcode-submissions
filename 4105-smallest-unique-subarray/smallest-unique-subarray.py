class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        base = 911382323
        mod1 = 10**9 + 7
        mod2 = 10**9 + 9

        def build(mod):
            prefix = [0] * (n + 1)
            power = [1] * (n + 1)

            for i, x in enumerate(nums):
                prefix[i + 1] = (prefix[i] * base + x) % mod
                power[i + 1] = power[i] * base % mod

            return prefix, power

        p1, pow1 = build(mod1)
        p2, pow2 = build(mod2)

        def get_hash(left, right, prefix, power, mod):
            return (
                prefix[right]
                - prefix[left] * power[right - left]
            ) % mod

        def check(k):
            freq = defaultdict(int)

            for i in range(n - k + 1):
                h1 = get_hash(i, i + k, p1, pow1, mod1)
                h2 = get_hash(i, i + k, p2, pow2, mod2)
                freq[(h1, h2)] += 1

            return any(count == 1 for count in freq.values())

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
