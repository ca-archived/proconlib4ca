from typing import List, Tuple
from heapq import heappush, heappop

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

    def append(self, x: Edge):
        list.append(x)

INF = 1 << 28

def dijkstra(graph: List[Edges], s: int) -> List[int]:
    n = len(graph)
    dist = [INF for _ in range(n)]

    pq: List[Tuple[int, int]] = []
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

if __name__ == '__main__':
    graph = [Edges() for _ in range(6)]

    graph[0].extend([Edge(1, 5), Edge(2, 4), Edge(3, 2)])
    graph[1].extend([Edge(0, 5), Edge(2, 2), Edge(5, 6)])
    graph[2].extend([Edge(0, 4), Edge(1, 2), Edge(3, 3), Edge(4, 2)])
    graph[3].extend([Edge(0, 2), Edge(2, 3), Edge(4, 6)])
    graph[4].extend([Edge(2, 2), Edge(3, 6), Edge(5, 4)])
    graph[5].extend([Edge(1, 6), Edge(4, 4)])

    print(dijkstra(graph, 0))