from heapq import heappush, heappop


# グラフ定義
class Edge:
    def __init__(self, to: int, cost: int):
        self._to = to
        self._cost = cost

    @property
    def to(self):
        return self._to

    @property
    def cost(self):
        return self._cost


class Edges(list):
    def __init__(self):
        list.__init__(self)


INF = 1 << 28


# ここから本実装
def dijkstra(graph, s: int):
    n = len(graph)
    dist = [INF for _ in range(n)]

    pq = []
    heappush(pq, (0, s))
    dist[s] = 0

    while pq:
        (cost, cur) = heappop(pq)

        if dist[cur] != cost:
            continue

        for next in graph[cur]:
            if dist[next.to] > cost + next.cost:
                heappush(pq, (cost + next.cost, next.to))
                dist[next.to] = cost + next.cost

    return dist
