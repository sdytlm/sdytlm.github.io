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
    public List<TreeNode> generateTrees(int n) {
        if(n==0) return new ArrayList<TreeNode>();
        return dfs(1,n);                
    }

    public List<TreeNode> dfs(int start, int end){
        List<TreeNode> ret = new ArrayList<TreeNode>();
        if(start>end){
            ret.add(null);
            return ret;
        }
        for(int rootval = start; rootval<=end; rootval++){
            List<TreeNode> leftList, rightList;
            leftList = dfs(start,rootval-1);
            rightList = dfs(rootval+1, end);
        
            for(TreeNode leftNode :leftList){
                for(TreeNode rightNode : rightList){
                    TreeNode root = new TreeNode(rootval);
                    root.left = leftNode;
                    root.right = rightNode;
                    ret.add(root);
                
                }
            }
        }

        return ret;
    }
}
