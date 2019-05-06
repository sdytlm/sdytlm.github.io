class Solution(object):
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
        # 两个长方形面积和
        area = (C-A)*(D-B) + (G-E)*(H-F)

        if A > G or C < E or D < F or B > H:
            return area
        else:
            return area - (min(D,H)-max(B,F)) * (min(C,G) - max(A,E))
       
