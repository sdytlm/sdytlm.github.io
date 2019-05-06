public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[][] matrix = new int[numCourses][numCourses];
        int[] indegree = new int[numCourses];

        // 初始化matrix and indegree
        for(int i = 0; i<prerequisites.length; i++){
            int prev = prerequisites[i][1];
            int course = prerequisites[i][0];
            if(matrix[prev][course] == 0)
                indegree[course] ++;
            matrix[prev][course] = 1;
        }
        Queue<Integer> queue = new LinkedList<Integer>();
        // 把indegree为0的点 插入queue
        for(int i=0; i<indegree.length;i++)
            if(indegree[i]==0) queue.offer(i);

        // 一次删除queue element
        int count = 0;
        while(!queue.isEmpty()){
            int course = queue.poll();
            count++;
            // 删除course 已经插入和course有关并且indegree[i]==0点.
            for(int i=0;i<numCourses;i++){
                if(matrix[course][i] == 1){
                    indegree[i]--;
                    if(indegree[i]==0) queue.offer(i);
                
                }
            
            }
        
        
        }
        return count == numCourses;
    }
}
