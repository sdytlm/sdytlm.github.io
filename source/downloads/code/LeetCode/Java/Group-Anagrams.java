public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if(strs==null || strs.length==0) return new ArrayList<List<String>>();
        Map<String, List<String>> map = new HashMap<String, List<String>>();
        Arrays.sort(strs);
        for(String s : strs){
            char[] char_s = s.toCharArray();
            Arrays.sort(char_s);
            String key_val = String.valueOf(char_s);
            if(!map.containsKey(key_val))
                map.put(key_val, new ArrayList<String>());
            map.get(key_val).add(s);
        }
        return new ArrayList<List<String>>(map.values());
    }
}
