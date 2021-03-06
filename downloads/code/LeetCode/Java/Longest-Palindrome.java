public class Solution {
    public int longestPalindrome(String s) {
        if(s==null || s.length()==0)
            return 0;
        HashSet<Character> hs = new HashSet<Character>();
        int count = 0;
        
        for(int i=0; i<s.length();i++){
            if(hs.contains(s.charAt(i))){
                count++;
                hs.remove(s.charAt(i));        
            }
            else
                hs.add(s.charAt(i));
        }
        if(!hs.isEmpty()) return 2*count+1;
        else return 2*count;     
    }
}
