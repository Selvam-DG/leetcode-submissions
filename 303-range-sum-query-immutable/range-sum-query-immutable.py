class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefixSum =  [0] * len(nums)
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            self.prefixSum[i] = curr_sum
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        return self.prefixSum[right] - self.prefixSum[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)