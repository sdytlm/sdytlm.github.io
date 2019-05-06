public class Solution {
    public int mySqrt(int x) {
        int l = 0;
        int r = Integer.MAX_VALUE;
        if(x==0)
            return 0;
        while (l<=r){
            int mid = l+(r-l)/2;
            if (mid > x/mid)
                r = mid-1;
            else{
                if (mid+1 >x/(mid+1))
                    return mid;
                l = mid+1;
            }   
        
        }
        return l-1;
    }
}

