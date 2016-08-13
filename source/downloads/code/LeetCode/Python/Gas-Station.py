class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        bal = 0
        start = 0
        for i in range(len(gas)):
            bal += gas[i] - cost[i]
            if bal < 0:
                start = i+1
                bal = 0
        if sum(gas) - sum(cost) >=0:
            return start
        else:
            return -1

