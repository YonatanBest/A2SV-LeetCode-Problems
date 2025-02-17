# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:        
        arr = [0]*len(s)

        for left, right, k in shifts:
            if k == 1:
                arr[left] += 1
                if right + 1 < len(arr):
                    arr[right+1] -=1
            else:
                arr[left] -= 1
                if right + 1 < len(arr):
                    arr[right+1] +=1

        for i in range(1, len(s)):
            arr[i] += arr[i - 1]

        for j in range(len(s)):
            arr[j] += ord(s[j]) - 97

        for x in range(len(arr)):
            arr[x] = chr((arr[x] % 26) + 97)
        
        return "".join(arr)
