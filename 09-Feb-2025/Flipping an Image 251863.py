# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            i = 0
            j = len(image[row]) - 1
            while i < j:
                image[row][i], image[row][j] = image[row][j], image[row][i]
                i += 1
                j -= 1
        for row in range(len(image)):
            for col in range(len(image)):
                image[row][col] = 0 if image[row][col] else 1
        return image