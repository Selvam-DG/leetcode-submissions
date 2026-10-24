class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def convert(s:str):
            month = int(s[:2])
            date = int(s[3:])

            return sum(days[:month-1]) + date
        
        alice_start = convert(arriveAlice)
        alice_end = convert(leaveAlice)
        bob_start = convert(arriveBob)
        bob_end = convert(leaveBob)

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)

        return max(0, end-start+1)