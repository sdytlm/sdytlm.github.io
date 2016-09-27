public class Solution {
    public boolean isSubsequence(String s, String t) {
        int i=0;
        int j=0;
        if (t.length() < s.length())
            return false;

        while (i<s.length() && j<t.length()){
            if (s.charAt(i)==t.charAt(j)){
                i ++;
            }  
            j++;
        }
        if(i==s.length())
            return true;
        return false;
    }
}
