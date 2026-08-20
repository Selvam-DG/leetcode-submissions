class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = dict()
        n = len(nums)
        for i in range(n):
            need = target-nums[i]
            if need in hmap:
                return [hmap[need], i]
            hmap[nums[i]] = i
        