public class Solution {
    public int[] findRightInterval(Interval[] intervals) {
        // TreeMap<start, index>
        TreeMap<Integer, Integer> map = new TreeMap<>();
        int[] ret = new int[intervals.length];
        // init TreeMap
        for(int i=0;i<intervals.length;i++)
            map.put(intervals[i].start, i);

        // 便利intervals, 找到最小的比intervals[i].end大的entry
        for(int i=0;i<intervals.length;i++){
            Integer key = map.ceilingKey(intervals[i].end);
            ret[i] = key!=null ? map.get(key) : -1;
        }
        return ret;
    }
}
