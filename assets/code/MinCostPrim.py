import heapq

class Solution(object):
    def minCostConnectPoints(self, points):
        N = len(points) 
        adj = {i:[] for i in range(N)} # para cada i, tem vizinho lista de [cost, node]

        #arestas
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        #prim
        totalCost = 0
        visited = set()
        minHeap = [(0, 0)] # (cost, node)

        while len(visited) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            totalCost += cost
            visited.add(i)
            for vizcost, viz in adj[i]:
                heapq.heappush(minHeap, [vizcost, viz])
        return totalCost
    

# Testes
print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])) 