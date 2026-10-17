
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        def digitSum(num):
            return sum(int(d) for d in str(num))

        # Step 1: Find the required sorted order
        sorted_nums = sorted(nums, key=lambda x: (digitSum(x), x))

        # Step 2: Map each number to its target index
        target = {num: i for i, num in enumerate(sorted_nums)}

        # Step 3: Count swaps using cycle detection
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = target[nums[j]]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps
