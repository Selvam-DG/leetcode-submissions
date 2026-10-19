class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        result = []
        smaller = 0
        equal = 0
        for num in nums:
            if num < target:
                smaller += 1
            if num == target:
                equal += 1
        
        
        for n in range(smaller, smaller+equal):
            result.append(n)

        return result
            