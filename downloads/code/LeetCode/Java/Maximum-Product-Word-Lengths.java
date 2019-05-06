public class Solution {
    public int maxProduct(String[] words) {
        int n = words.length;
        // 每个elements 有26bit, 一个bit表示words[i]中的一个字母是否存在
        int[] elements = new int[n];
        for(int i=0; i<n; i++){
            String s = words[i];
            for(int j=0;j<s.length();j++){
                elements[i] |= 1<<(s.charAt(j)-'a');
            }
        }
        int ret = 0;
        for(int i=0; i<n; i++){
            for(int j=i+1;j<n;j++){
                if((elements[i] & elements[j]) == 0)
                    ret = Math.max(ret, words[i].length()*words[j].length());
            
            }
        
        }
        return ret;

    }
}
