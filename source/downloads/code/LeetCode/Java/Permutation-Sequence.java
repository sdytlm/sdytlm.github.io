public class Solution {
    public String getPermutation(int n, int k) {
        String ret = "";
        ArrayList<Integer> list = new ArrayList<Integer>();
    
        for(int i=1;i<=n;i++){
            list.add(i);
        }
        int factor = 1;
        // calculate n!
        for (int i=1;i<n;i++)
            factor = factor*i;
        
        k = k-1;
        for (int i=n-1;i>=0;i--){
            ret += Integer.toString(list.get(k/factor));
            list.remove(k/factor);
            k = k%factor;
            if(i!=0)
                factor = factor/i;
        
        }
        return ret;

    }
}
