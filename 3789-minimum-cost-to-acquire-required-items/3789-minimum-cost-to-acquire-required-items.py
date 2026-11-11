
class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        
        # If buying both individually is cheaper
        if costBoth >= cost1 + cost2:
            return need1 * cost1 + need2 * cost2

        # Buy type 3 items for the common requirement
        common = min(need1, need2)
        
        ans = common * costBoth

        # Fulfill the remaining requirement
        if need1 > need2:
            ans += (need1 - need2) * min(cost1, costBoth)
        else:
            ans += (need2 - need1) * min(cost2, costBoth)

        return ans
