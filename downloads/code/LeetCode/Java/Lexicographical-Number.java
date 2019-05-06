public class Solution {
    public List<Integer> lexicalOrder(int n) {
        int cur = 1;
        List<Integer> ret = new ArrayList<Integer>();
        for(int i=1;i<=n;i++){
            ret.add(cur);
            if(cur*10 <= n)
                cur = cur*10;
            else if (cur% 10 != 9 && cur+1<=n)
                cur = cur+1;
            else{
                while((cur/10) % 10 == 9)
                    cur = cur / 10;
                cur = cur/10+1;
            }
        }
        return ret;    
    }
}
