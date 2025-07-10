def minCostClimbingStairs(cost):
    memo = {}

    def _minCost(i):
        if i >= len(cost):
            return 0
        if i in memo:
            return memo[i]
        memo[i] = cost[i] + min(_minCost(i + 1), _minCost(i + 2))
        return memo[i]

    return min(_minCost(0), _minCost(1))


def minCostClimbingStairsIterativeDP(cost):
    if len(cost) == 0:
        return 0
    if len(cost) == 1:
        return cost[0]

    prev2 = cost[0]
    prev1 = cost[1]

    for i in range(2, len(cost)):
        curr = cost[i] + min(prev1, prev2)
        prev2 = prev1
        prev1 = curr

    return min(prev1, prev2)


cost = [10, 15, 20]
print(minCostClimbingStairs(cost))
print(minCostClimbingStairsIterativeDP(cost))
# [10, 15, 20]
#  i
