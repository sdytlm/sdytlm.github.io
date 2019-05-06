class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # Create a dict with list in the value part
        target = collections.defaultdict(list)
        for i,j in sorted(tickets)[::-1]:
            targets[i] += j,

        ret = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            # find destination
            ret.append(airport)
        visit('JFK')
        return ret[::-1]


