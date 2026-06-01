class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        res= 0
        for i, v in enumerate(cost):
            if (i+1)%3==0:
                print(cost[i])
                res+=cost[i]
        return sum(cost) - res


