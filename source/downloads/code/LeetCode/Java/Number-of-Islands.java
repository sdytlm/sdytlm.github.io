public class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        if(m==0) return 0;
        int n = grid[0].length;
        int ret = 0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j] == '1'){
                    ret++;
                    dfs(grid,i,j);
                }
            }
        }
        return ret;
    }

    public void dfs(char[][] grid, int m, int n){
        if(m<0 || m>=grid.length || n<0 || n>=grid[0].length || grid[m][n]!='1')
            return ;
        grid[m][n] = '0';
        dfs(grid,m-1,n);
        dfs(grid,m+1,n);
        dfs(grid,m,n-1);
        dfs(grid,m,n+1);
    }
}
