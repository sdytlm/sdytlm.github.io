public class Solution {
    public int minDepth(TreeNode root) {
        if(root==null)
            return 0;
        return dfs(root,1);
    }
    public int dfs(TreeNode root, int depth){
        if(root.left==null && root.right==null)
            return depth;
        if(root.left!=null && root.right!=null)
            return Math.min(dfs(root.left, depth+1), dfs(root.right, depth+1));
        else if (root.left==null)
            return dfs(root.right, depth+1);
        else
            return dfs(root.left, depth+1);
        
    }
}
