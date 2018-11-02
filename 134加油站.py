class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        index = 0
        current = 0
        for i in range(len(gas)):
            current += gas[i]-cost[i]
            if current < 0:
                current = 0
                index = i+1
        return index