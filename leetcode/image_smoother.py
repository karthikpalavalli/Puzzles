import math

class Solution:
    def imageSmoother(self, M):
        smoothed_image = [[0] * len(M)] * len(M)

        for i in range(len(M)):
            for j in range(len(M)):
                surrounding_pixels = list()

                surrounding_pixels.append(M[i][j])

                if i - 1 >= 0 and j - 1 >= 0:
                    surrounding_pixels.append(M[i - 1][j - 1])

                if i - 1 >= 0:
                    surrounding_pixels.append(M[i - 1][j])

                if i - 1 >= 0 and j + 1 < len(M):
                    surrounding_pixels.append(M[i - 1][j + 1])

                if 