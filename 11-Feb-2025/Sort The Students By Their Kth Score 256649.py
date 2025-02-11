# Problem: Sort The Students By Their Kth Score - https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        dic = {}
        arr = []
        for i in range(len(score)):
            arr.append(score[i][k])
            dic[score[i][k]] = i
        arr.sort(reverse=True)
        for j in range(len(arr)):
            dic[score[j][k]] = dic[arr[j]]
            score[j], score[dic[arr[j]]] = score[dic[arr[j]]], score[j]
        return score