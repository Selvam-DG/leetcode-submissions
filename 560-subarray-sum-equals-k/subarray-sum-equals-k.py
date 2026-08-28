class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = dict()
        prefix_map[0] =  1
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num
            need = curr_sum - k
            count += prefix_map.get(need, 0)
            prefix_map[curr_sum] = 1 + prefix_map.get(curr_sum, 0)

        return count