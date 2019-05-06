public class Solution {
    public List<Integer> diffWaysToCompute(String input) {
        List<Integer> ret = new LinkedList<Integer>();
        for(int i=0;i<input.length();i++){
            if(input.charAt(i)=='+' || input.charAt(i)=='*' ||
               input.charAt(i)=='-'){
               
               List<Integer> left = diffWaysToCompute(input.substring(0,i));
               List<Integer> right = diffWaysToCompute(input.substring(i+1));

               for(int p1 : left){
                   for(int p2 : right){
                        int c = 0;
                        if(input.charAt(i) == '+')
                            c = p1+p2;
                        if(input.charAt(i) == '*')
                            c = p1*p2;
                        if(input.charAt(i) == '-')
                            c = p1-p2;
                   
                        ret.add(c);
                   }
               }
            }

        }       
        if(ret.size()==0)
            ret.add(Integer.valueOf(input));
        return ret;
    }
}
