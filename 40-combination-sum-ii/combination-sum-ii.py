class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        n = len(candidates)

        def recursive(index, curr_sum, temp_arr):
            if curr_sum > target:
                return
            if curr_sum == target:
                result.append(temp_arr.copy())
                return
            
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                if curr_sum + candidates[i] > target:
                    break
                
                temp_arr.append(candidates[i])

                recursive(i+1, curr_sum + candidates[i], temp_arr)

                temp_arr.pop()
        recursive(0, 0 , [])

        return result