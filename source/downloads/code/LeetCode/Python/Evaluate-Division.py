class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # graph: dict<dict<edge1, edge2>, value>
        graph = collections.defaultdict(lambda: collections.defaultdict(int))         
        for (s,t), v in zip(equations, values):
            graph[s][t] = v
            graph[t][s] = 1.0/v

        for k in graph:
            graph[k][k] = 1.0
            for s in graph:
                for t in graph:
                    if graph[s][k] and graph[k][t]:
                        graph[s][t] = graph[s][k] * graph[k][t]
        ret = []
        for s,t in queries:
            ret.append(graph[s][t] if graph[s][t] else -1.0)
        return ret
