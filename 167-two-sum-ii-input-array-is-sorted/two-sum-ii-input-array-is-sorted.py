class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        l = 0
        r = n-1

        while l < r:
            total = numbers[l] + numbers[r]

            if total == target:
                return [l+1, r+1]
            elif total <  target:
                l += 1
            else:
                r -= 1
        return [-1, -1]