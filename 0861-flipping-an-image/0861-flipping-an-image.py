class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            i = 0
            j = len(image[row]) - 1
            while i < j:
                image[row][i], image[row][j] = image[row][j], image[row][i]
                image[row][i]^= 1
                image[row][j]^= 1
                i += 1
                j -= 1
            if len(image[row]) % 2:
                image[row][j]^= 1
        return image