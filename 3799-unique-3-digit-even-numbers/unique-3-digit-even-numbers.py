class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10
        for digit in digits:
            freq[digit] += 1
        ans = 0
        for num in range(100, 1000,2):
            count = [0]* 10

            while num > 0:
                count[num % 10] += 1
                num = num // 10
            
            if all(count[d] <= freq[d] for d in range(0,10)):
                ans += 1
        
        return ans
        