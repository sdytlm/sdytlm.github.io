/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    
    List<List<Integer>> ret = new LinkedList<List<Integer>>();
    List<Integer> tmp = new LinkedList<Integer>();
 
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        if (root == null)
            return ret;
        dfs(root, sum);
        return ret;       
    }

    public void dfs(TreeNode root, int sum){
        tmp.add(root.val);
        if (sum == root.val && root.left==null && root.right==null) {
            ret.add(new LinkedList(tmp));       
            return ;    
        }
        
        if (root.left != null){
            dfs(root.left, sum-root.val);
            tmp.remove(tmp.size()-1);
        }
        if (root.right != null){
            dfs(root.right, sum-root.val);
            tmp.remove(tmp.size()-1);
        }
        
    }
}
