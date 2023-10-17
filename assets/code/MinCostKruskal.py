class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        edges = []
		
        for i in range(n):
            for j in range(i+1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((d, i, j))
        
        edges.sort()
        
        roots = [i for i in range(n)]
        
        def find(v):
            if roots[v] != v:
                roots[v] = find(roots[v])
            return roots[v]
        
        def union(u, v):
            p1 = find(u); p2 = find(v)
            if p1 != p2:
                roots[p2] = roots[p1]
                return True
            return False
        
        res = 0
        for d, u, v in edges:
            if union(u, v):
                res += d
        return res
    
# Testes

print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])) 
#saída =20

print(Solution().minCostConnectPoints([[3,12],[-2,5],[-4,1]]))