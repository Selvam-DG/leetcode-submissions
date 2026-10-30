class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u,v,w in edges:
            graph[u].append((v,w))

        dist = [[float('inf')]*(k+1) for _ in range(n)]

        heap = [(0,0,1)]
        dist[0][1] = 0

        while heap:
            cost, node, count = heapq.heappop(heap)

            if cost > dist[node][count]:
                continue
            
            if node == n-1:
                return cost
            
            for neighbour, weight in graph[node]:
                if labels[node] == labels[neighbour]:
                    new_count = count+  1
                else:
                    new_count = 1
                
                if new_count > k:
                    continue
                
                new_cost = cost + weight

                if new_cost < dist[neighbour][new_count]:
                    dist[neighbour][new_count] = new_cost

                    heapq.heappush(heap, (new_cost, neighbour, new_count))
            
        return -1
