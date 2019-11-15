class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area_1 = (C - A) * (D - B)
        area_2 = (G - E) * (H - F)

        l = min(C, G) - max(A, E)
        b = min(D, H) - max(B, F)

        area_total = area_1 + area_2

        if l > 0 and b > 0:
            area_total -= l*b

        return area_total
