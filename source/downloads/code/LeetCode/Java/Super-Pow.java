public class Solution {
    public int superPow(int a, int[] b) {
        int ret=1;
        for(int i=b.length-1; i>=0; i--){
            ret = ret*pow(a,b[i],1337)%1337;
            a = pow(a,10,1337);
        }
        return ret;
    }
    // 计算a^b%c
    public int pow(int a, int b, int c){
        long ret = 1;
        long p = a;
        while(b>0){
            if((b&1)==1)
                ret = (ret*p)%c;
            p = (p*p)%c;
            b = b>>1;
        }
        return (int)(ret%c);
    }
}

