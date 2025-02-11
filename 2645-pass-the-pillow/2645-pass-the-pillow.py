class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 1
        check = True
        times = 1
        j = 0
        arr = []
        while times <= time:
            arr.append(str(i))
            if i < n and check:
                i += 1
            elif i > 1:
                i -= 1
                check = False
            else:
                i += 1
                check = True
            times += 1
        arr.append(str(i))
        print(" --> ".join(arr))
        return i
        
