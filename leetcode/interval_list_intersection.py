from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ptr_a = ptr_b = 0
        list_intersection = list()

        while ptr_a != len(A) and ptr_b != len(B):
            intersection_start = max(A[ptr_a][0], B[ptr_b][0])
            intersection_end = min(A[ptr_a][1], B[ptr_b][1])

            if intersection_start <= intersection_end:
                list_intersection.append([intersection_start, intersection_end])

            if A[ptr_a][1] <= B[ptr_b][1]:
                ptr_a += 1

            else:
                ptr_b += 1

        return list_intersection
