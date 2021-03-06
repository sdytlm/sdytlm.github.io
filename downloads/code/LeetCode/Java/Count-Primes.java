public class Solution {
    public int countPrimes(int n) {
       boolean[] isprimes = new boolean[n];
       int count = 0;
       for(int i=2;i<n;i++){
            if(isprimes[i]==false){
                count ++;
                for(int j=2;i*j<n;j++)
                    isprimes[i*j] = true;
            }
       }
       return count;
    }
}
