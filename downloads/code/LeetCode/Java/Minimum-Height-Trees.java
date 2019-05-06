public class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if(n==1) return Collections.singletonList(0);
        List<Integer> leaves = new ArrayList<>(n);
        // <节点: 所有和节点相连的其他节点组成的set
        List<Set<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; ++i) adj.add(new HashSet<>());
        for(int[] edge : edges){
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }
        // leaves: 记录所有的叶子节点
        for(int i=0;i<n;i++){
            if(adj.get(i).size()==1)
                leaves.add(i);
        }

        // BFS
        while(n>2){
            n = n-leaves.size();
            List<Integer> newleaves = new ArrayList<>();
            // 找到leave并把和他相邻的点全部删除
            for(int leave: leaves){
                int j=adj.get(leave).iterator().next();
                adj.get(j).remove(leave);
                if(adj.get(j).size()==1) newleaves.add(j);
            }
            leaves = newleaves;
        }
        return leaves;

    }
}
