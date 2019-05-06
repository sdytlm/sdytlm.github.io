public class Solution {
    public boolean isPalindrome(int x) {
        if (x<0) return false;
        int p = x;
        int q = 0;
        //　ｑ是ｘ的反转版本，除了最高位，因为怕overflow
        while (p>=10){
            q = 10*q + p%10;
            p = p/10;
        }
        return (q==x/10) && (p == x%10);
    }
}
