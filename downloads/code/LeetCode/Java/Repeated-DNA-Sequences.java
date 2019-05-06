public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        int[] dna = new int[26];
        dna['A'-'A'] = 0;
        dna['C'-'A'] = 1;
        dna['G'-'A'] = 2;
        dna['T'-'A'] = 3;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        List<String> ret = new LinkedList<String>();
        int sum = 0;
        for(int i=0;i<s.length();i++){
            sum = ((sum<<2) + dna[s.charAt(i)-'A'])& 0xfffff;
            if(i<9)
                continue;
            if(map.containsKey(sum))
                map.put(sum, map.get(sum)+1);
            else
                map.put(sum,1);
            if(map.get(sum)==2)
                ret.add(s.substring(i-9,i+1));
        }
        return ret;
    }
}
