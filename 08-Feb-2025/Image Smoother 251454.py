# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        dir = [(1,0), (-1, 0), (0,1), (0,-1), (1,1), (-1,-1), (1, -1), (-1, 1)]
        new = [[0 for k in range(len(img[0]))] for c in range(len(img))]

        for i in range(len(img)):
            for j in range(len(img[i])):
                ans = img[i][j]
                counter = 1
                for di in dir:
                    if i + di[0] >= 0 and j + di[1] >= 0 and i + di[0] < len(img) and j + di[1] < len(img[0]):
                        counter += 1
                        ans += img[i + di[0]][j + di[1]]
                new[i][j] = ans // counter
        return new