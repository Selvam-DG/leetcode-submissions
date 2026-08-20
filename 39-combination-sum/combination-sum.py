class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def recursive(curr_sum, index, temp_arr):
            if curr_sum == target:
                result.append(temp_arr.copy())
                return
            if index >= len(candidates) or curr_sum > target:
                return
            
            temp_arr.append(candidates[index])
            recursive(curr_sum + candidates[index], index, temp_arr)

            temp_arr.pop()
            recursive(curr_sum, index + 1, temp_arr)

        recursive(0, 0, [])

        return result