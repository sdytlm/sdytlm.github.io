public class Solution {
    public int[][] reconstructQueue(int[][] people) {
        // override compare
        Arrays.sort(people, new Comparator<int[]>(){
            public int compare(int[] o1, int[] o2)
                {
                    return o1[0]!=o2[0]? o2[0]-o1[0]: o2[1]-o1[1];
                }
            });

            List<int[]> ret = new LinkedList<>();
            for(int[] cur: people)
                ret.add(cur[1], cur);
            return ret.toArray(new int[people.length][]);
    }
}
