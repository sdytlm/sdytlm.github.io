public class Solution {
    public boolean canMeasureWater(int x, int y, int z) {
        if (x+y<z) return false;
        // case: x==0 or y==0
        if (x==z || y==z || x+y==z) return true;
        return z%GCD(x,y)==0;        
    }

    public int GCD(int a, int b){
        while(b!=0){
            int tmp = b;
            b = a%b;
            a = tmp;
        }
        return a;
    }

}
