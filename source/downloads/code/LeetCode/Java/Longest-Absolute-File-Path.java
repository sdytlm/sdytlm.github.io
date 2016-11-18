public class Solution {
    public int lengthLongestPath(String input) {
        // 把输入按照\n分开
        String[] parts = input.split("\n");
        
        int[] stack = new int[paths.length+1];
        //stack[i]: 坐标为i的"\t"对应的路径长度
        int maxLen = 0;
        for(String s : parts){
            int lev = s.lastIndexOf("\t")+1;
            int curLen = stack[lev+1] = stack[lev]+s.length()-lev+1;
        
        }
    }
}
