class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        back_two = 1
        back_one = 1
        for i in range(2, n+1):
            temp = back_two + back_one
            back_two = back_one
            back_one = temp

        return back_one