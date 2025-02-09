class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = list(reversed(image[i]))
        for row in range(len(image)):
            for col in range(len(image)):
                image[row][col] = 0 if image[row][col] else 1
        return image