INF = float("inf")

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = grid[0][:]
        
        for i in range(1, m):
            for j in range(n):
                min_cost = INF
                for k in range(n):
                    min_cost = min(min_cost, dp[i - 1][k] + grid[i][j] + moveCost[grid[i - 1][k]][j])
                dp[i][j] = min_cost
        
        return min(dp[-1])
                
        