class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = dict()

        for i in range(len(reservedSeats)):
            row, seat = reservedSeats[i]
            if seat >= 2 and seat <= 9:
                if row not in reserved:
                    reserved[row] = set()
                reserved[row].add(seat)
        #for uncompletey touch row, 2 times of 4 group can be fit
        result = (n - len(reserved)) * 2 

        for row, seats in reserved.items():
            left = True
            right = True
            middle = True
            for seat in range(2,6):
                if seat in seats:
                    left = False
                    break
            
            for seat in range(6,10):
                if seat in seats:
                    right = False
                    break
            if left:
                result += 1
            if right:
                result += 1
            if not left and not right:
                for seat in range(4,8):
                    if seat in seats:
                        middle = False
                        break
                if middle:
                    result += 1
        return result
            
