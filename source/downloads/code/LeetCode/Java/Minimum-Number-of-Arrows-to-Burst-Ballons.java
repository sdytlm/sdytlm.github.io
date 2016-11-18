public class Solution {
    public int findMinArrowShots(int[][] points) {
        if(points == null || points.length==0) return 0;
        Arrays.sort(points,(x,y)->x[0]==y[0] ? x[1]-y[1] : x[0]-y[0]);
        // 需要的箭数
        int count = 1;
        // 要射中之前的气球，箭的最大范围
        int arrowLimit = points[0][1];
        for(int i=0; i<points.length; i++){
            if(arrowLimit >= points[i][0]){
                // 可以设中
                arrowLimit = Math.min(points[i][1],arrowLimit);
            }
            else{
                // 不能设中
                count ++;
                arrowLimit = points[i][1];
            }
        }
        return count;   
    }
}
