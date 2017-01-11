/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     List<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    // 已经创建过的node,label 映射<label, Node>
    private HashMap<Integer, UndirectedGraphNode> map = new HashMap<>();
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        return clone(node);    
    }
    public UndirectedGraphNode clone(UndirectedGraphNode node){
        if(node==null) return null;
        if(map.containsKey(node.label)) return map.get(node.label);
        
        // 不在map中，说明之前没有给这个节点创建object.
        UndirectedGraphNode newNode = new UndirectedGraphNode(node.label);
        map.put(node.label, newNode);
        // copy neighbors
        for(UndirectedGraphNode neighbor : node.neighbors){
            newNode.neighbors.add(clone(neighbor));
        }
        return newNode;
    }
}
