class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Algorithm
        # bruteforce
        # i ranges from 0 to n
        # j ranges from i to n
        # count no of 1 in s: if count > k break
        # store the min length 
        
        # better approach - two pointer + window expansion
        # l = 0,, r from 0 to n
        # if char is 1 and count_1 < k, then increemnt the count_1
        # if count_1 > k, do while count_1 <= k -> shrink the window by remov the left element and update the minimun window with l,r values


        n = len(s)

        l = 0
        count_1 = 0
        ans = ""

        for r in range(n):
            if s[r] == "1":
                count_1 += 1
            while count_1 > k:
                if  s[l] == "1":
                    count_1 -= 1
                l += 1
            
            while count_1 == k and l < r and s[l] == "0":
                l += 1
            
            if count_1 == k:
                curr = s[l:r+1]
                if (ans =="" or len(curr) < len(ans) or (len(curr)== len(ans) and curr < ans)):
                    ans = curr
        
        return ans