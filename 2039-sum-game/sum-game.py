class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        left_sum = 0
        right_sum = 0
        left_question = 0
        right_question = 0

        mid = n // 2
        for i in range(mid):
            if num[i] == '?':
                left_question += 1
            else:
                left_sum += int(num[i])
        for i in range(mid, n):
            if num[i] =='?':
                right_question += 1
            else:
                right_sum += int(num[i])
        diff = left_sum - right_sum
        return 2*diff != 9*(right_question-left_question)
            

        