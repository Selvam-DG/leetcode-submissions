class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        pairs = sorted((num, i) for i,num in enumerate(nums))

        ans = nums[:]

        start = 0
        while start < n:
            end = start
            while end + 1 < n and pairs[end+1][0] -pairs[end][0] <= limit:
                end += 1
            
            values = []
            indices = []

            for j in range(start, end+1):
                values.append(pairs[j][0])
                indices.append(pairs[j][1])
            indices.sort()

            for index, value in zip(indices, values):
                ans[index] = value
            start = end + 1
        
        return ans
