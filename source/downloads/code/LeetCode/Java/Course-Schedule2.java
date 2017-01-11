public class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] ret = new int[numCourses];
        // 数组链表表示DAG: 课程x的前导课都在graph[x]中
        ArrayList<Integer>[] graph = new ArrayList[numCourses];
        // 入度数组
        int[] indegree = new int[numCourses];
        // 初始化indegree 和　graph
        for(int i=0; i<prerequisites.length; i++){
            if(graph[prerequisites[i][1]]==null)
                graph[prerequisites[i][1]] = new ArrayList<Integer>();
            graph[prerequisites[i][1]].add(prerequisites[i][0]);
            indegree[prerequisites[i][0]]++;
        }
        Queue<Integer> queue = new LinkedList<Integer>();
        // 把所有入度为０的加入queue
        for(int i=0; i<indegree.length; i++){
            if(indegree[i]==0)
                queue.add(i);
        }

        int idx = 0;
        while(!queue.isEmpty()){
            Integer cur = queue.poll();
            ret[idx++] = cur;
            // 这个课程没有前导了
            if(graph[cur]==null) continue;
            for (Integer nextIdx : graph[cur]){
                // 不管是不是０，indegree[next]--都会执行
                if(--indegree[nextIdx]==0)
                    queue.offer(nextIdx);
            
            }
        }
        return idx != numCourses ? new int[0] : ret;
    }
}
