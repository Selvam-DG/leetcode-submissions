class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7

        oddCount = 0
        evenCount = 1
        currSum = 0
        result = 0
        for num in arr:
            currSum += num
            if currSum % 2 == 0:
                result = (result+oddCount) % MOD
                evenCount += 1
            
            else:
                result = (result+ evenCount) % MOD
                oddCount += 1
        
        return result
