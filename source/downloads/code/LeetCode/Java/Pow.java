public class Solution {
    public double myPow(double x, int n) {
        if(n==0)
            return 1;
        if(n==1)
            return x;
        if(n<0)
            return pow(1/x, -n);
        else
            return pow(x,n);
    }
    public double pow(double x, int n){
        if(n==0)
            return 1;
        double v = pow(x,n/2);
        if(n%2==0)
            return v*v;
        else
            return v*v*x;
    
    }

}
