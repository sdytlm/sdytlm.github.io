public class Solution {
    public int integerReplacement(int n) {
        int ret = 0;
        while(n!=1){
            if(n%2==0){
                n >>>= 1;
            }
            else if (n==3 || (n>>>1 & 1)==0)
                n--;
            else
                n++;
            ret ++;
        
        } 
        return ret;
    }
}
