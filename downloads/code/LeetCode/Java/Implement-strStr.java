public class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length()==0) return 0;
        if (haystack.length()==0) return -1;

        int n = haystack.length()-1;
        int m = needle.length()-1;
        for(int i=0;i<=n-m;i++){
            int j=0;
            int k = i;
            while (j<=m && haystack.charAt(k) == needle.charAt(j)){
                k+=1;
                j+=1;
            }
            if (j>m)
                return i;
        }
        return -1;
    }
}
