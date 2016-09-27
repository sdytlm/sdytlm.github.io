public class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int area = (G-E)*(H-F) + (C-A)*(D-B);
        if (A>G || B>H || D<F || C<E)
            return area;
        else
            return area-(Math.min(C,G)-Math.max(A,E))*(Math.min(D,H)-Math.max(B,F));        
    }
}
