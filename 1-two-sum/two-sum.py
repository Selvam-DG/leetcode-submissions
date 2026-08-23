class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = dict()

        for i, num in enumerate(nums):
            need = target-num

            if need in hmap:
                return [hmap[need], i]
            
            hmap[num] = i
        