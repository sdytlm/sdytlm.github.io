# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

 # Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def __init__(self):
        # hash_map{label:new_node}
        self.hash_map = {}

    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        # hash_map: {new_node:new_node.label)
        if node == None:
            return None
        if node.label in self.hash_map:
            return self.hash_map[node.label]
        # new node
        root = UndirectedGraphNode(node.label)
        # update hash_map
        self.hash_map[node.label] = root
        for neighbor in node.neighbors:
            root.neighbors.append(self.cloneGraph(neighbor))
        return root      
