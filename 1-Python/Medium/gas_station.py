# 10/14 - Greedy
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to
# its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
# Note: The solution is guaranteed to be unique.

class GasStation(object):
    # Test on LeetCode - 40ms
    # Idea:
    #   compute tank and track total to see whether solution exists
    #   if total < 0, restart from current position
    def can_complete_circuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        length = len(gas)
        tank = []
        total = 0
        for i in range(0, length):
            left = gas[i] - cost[i]
            tank.append(left)
            total += left
        if total < 0:
            return -1
        start = 0
        total = 0
        for i in range(0, length):
            total += tank[i]
            if total < 0:
                start = i + 1
                total = 0
        return start

    # 12/29 - Revisit (adapted from YX)
    # Idea:
    #   one scan: if tank < 0, update index to be the one before start.
    #   if total < 0, no way; else, index + 1
    def can_complete_circuit_revisit(self, gas, cost):
        tank, total, index = 0, 0, -1
        for i in range(0, len(gas)):
            dif = gas[i] - cost[i]
            total += dif
            tank += dif
            if tank < 0:
                tank = 0
                index = i
        if total < 0:
            return -1
        return index + 1


def main():
    test = GasStation()
    print test.can_complete_circuit([2, 3, 1], [3, 1, 2])

if __name__ == "__main__":
    main()
