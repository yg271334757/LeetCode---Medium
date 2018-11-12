class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area_ABCD = (C - A) * (D - B)
        area_EFGH = (G - E) * (H - F)
        cover_A = max(A,E)
        cover_B = max(B,F)
        cover_C = min(C,G)
        cover_D = min(D,H)
        width =  cover_C - cover_A
        height = cover_D - cover_B
        if width <= 0 or height <= 0:
            return area_ABCD + area_EFGH
        area_covered = width * height
        return area_ABCD + area_EFGH - area_covered