public class Solution {
    public char findTheDifference(String s, String t) {
        int n = t.length();
        char ret = t.charAt(n-1);
        for(int i = 0; i < n-1;i++){
            ret ^= t.charAt(i);
            ret ^= s.charAt(i);
        }
        return ret;
    }
}
