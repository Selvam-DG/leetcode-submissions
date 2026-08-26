class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        uniq_nums = set()

        for num in nums:
            uniq_nums.add(num)
        temp = k
        while temp in uniq_nums:
            temp += k
        
        return temp