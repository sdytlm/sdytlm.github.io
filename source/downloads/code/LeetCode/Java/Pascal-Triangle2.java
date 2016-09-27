public class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> ret = new ArrayList<Integer>();
        if(rowIndex < 0)
            return ret;

        for(int i=0;i<=rowIndex;i++){
            ret.add(0,1);
            for (int j=1;j<ret.size()-1;j++){
                ret.set(j,ret.get(j+1)+ret.get(j));
            }
        } 
        return ret;
    }
}
