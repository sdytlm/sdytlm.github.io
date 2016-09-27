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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        List<List<Integer>> ret = new LinkedList<List<Integer>>();
        if (root == null)
            return ret;
        
        // queue add
        queue.offer(root);

        while (!queue.isEmpty()){
            List<Integer> list = new LinkedList<Integer>();
            // 一层多少点
            int levelNums = queue.size();
            for (int i = 0;i<levelNums;i++){
                TreeNode top = queue.element();
                if (top.left != null)
                    queue.offer(top.left);
                if (top.right != null)
                    queue.offer(top.right);
                list.add(top.val);
                // 把点删掉
                queue.poll();
            }
            ret.add(0,list);
        }
        return ret;
    }

}
