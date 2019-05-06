public class Solution {
    public int compareVersion(String version1, String version2) {
        String[] s1 = version1.split("\\.");
        String[] s2 = version2.split("\\.");
        
        int n = Math.max(s1.length, s2.length);
        for (int i=0;i<n;i++){
            Integer n1 = i < s1.length? Integer.parseInt(s1[i]):0;
            Integer n2 = i < s2.length? Integer.parseInt(s2[i]):0;
            int compare = n1.compareTo(n2);
            if (compare != 0)
                return compare;
        }
        return 0;
    }

}
