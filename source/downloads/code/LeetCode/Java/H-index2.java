public class Solution {
    public int hIndex(int[] citations) {
        int r = citations.length-1;
        int l = 0;
        while(l<=r){
            int m = l+(r-l)/2;
            if(citations[m] < citations.length-m)
               l = m+1;
            else
               r = m-1; 
        }
        return citations.length-l;
    }
}
