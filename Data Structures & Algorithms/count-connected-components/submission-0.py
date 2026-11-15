class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
       

        def bfs(node):
            q = deque([node])
            visited[node] = True

            while q:
                cur = q.popleft()

                for nei in adj[cur]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)
            
        res = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                bfs(node)
                res += 1
            
        return res