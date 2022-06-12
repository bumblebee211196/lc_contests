INF = float("inf")

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        dist = [0 for _ in range(k)]
        res = INF
        
        def dfs(i):
            nonlocal res
            if i == n:
                res = min(res, max(dist))
                return
            # Stop bracnhing if the current unfairness is greater than the actual "res"
            if max(dist) >= res:
                return
            for j in range(k):
                dist[j] += cookies[i]
                dfs(i + 1)
                dist[j] -= cookies[i]
        
        dfs(0)
        return res
