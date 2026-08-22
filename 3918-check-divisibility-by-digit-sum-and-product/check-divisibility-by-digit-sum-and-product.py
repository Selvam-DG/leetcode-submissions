class Solution:
    def checkDivisibility(self, n: int) -> bool:

        temp = n
        sumup = 0
        product = 1

        while temp != 0:
            num = temp % 10
            temp = temp // 10
            sumup += num
            product *= num
        
        return n % (sumup + product) == 0
        

        