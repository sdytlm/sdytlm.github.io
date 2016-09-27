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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> ret = LinkedList<List<Integer>>();
        travel(root,ret,0); 
    }

    public void travel(TreeNode node, List<List<Integer>> ret, int level){
        if(node==null) return ;

        if(ret.size() <= level){
            List<Integer> newLevel = new LinkedList<Integer>();
            ret.add(newLevel);
        }

        List<Integer> collection = ret.get(level);
        if(level%2 == 0)
            collection.add(node.val);
        else
            collection.add(0,node.val);

        travel(node.left, ret, level+1);
        travel(node.right, ret, level+1);

    }
}
