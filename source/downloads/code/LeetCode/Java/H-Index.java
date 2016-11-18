public class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        // array2: 一篇文章的引用 -> 出现次数
        int[] array2 = new int[n+1];
        if(n==0) return 0;

        for(int c: citations){
            if(c >= n) array2[n] ++;
            else
                array2[c]++;
        }
        int ret = 0;
        // 便利array2找答案
        for(int i=n; i>=0; i--){
            // ret: citation 为i的出现次数
            ret += array2[i];
            if(ret >= i) return i;
        }
        return 0;
    }
}
