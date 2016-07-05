class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        children = [[] for i in range(n)]
        # put all node in "edges" into children
        for edge in edges:
            children[edge[0]].append(edge[1])
            children[edge[1]].append(edge[0])

        # find leaves
        leaves = [x for x in range(n) if len(children[x]) <=1]

        # remove leaves
        while n>2:
            n -= len(leaves)
            newleaves = []
            for i in leaves:
                for node in children[i]:
                    children[node].remove(i)
                    # found new leave after remove. 
                    if len(children[node]) == 1:
                        newleaves.append(node)
            leaves = newleaves
        return leaves
