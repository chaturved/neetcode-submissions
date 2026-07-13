class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total, index = 0, 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            total += (g - c)
            if total < 0:
                total = 0
                index = i + 1
        
        return index
