import heapq
import sys

INF = sys.maxsize

input = sys.stdin.readline

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

K, E = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next, weight in graph[now]:
            new_dist = dist + weight
            if new_dist  < distance[next]:
                distance[next] = new_dist
                heapq.heappush(q, (new_dist, next))

    return distance

# dijkstra(K)
# print(distance)
dist_from_1  = dijkstra(1)
dist_from_v1 = dijkstra(K)
dist_from_v2 = dijkstra(E)

path1 = dist_from_1[K] + dist_from_v1[E] + dist_from_v2[N]
path2 = dist_from_1[E] + dist_from_v2[K] + dist_from_v1[N]

ans = min(path1, path2)

if ans >= INF:
    print(-1)
else:
    print(ans)