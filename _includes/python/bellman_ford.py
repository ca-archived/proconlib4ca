
# グラフ定義
class Edge:
    def __init__(self, f: int, t: int, cost: int):
        self._t = t
        self._cost = cost
        self._f = f

    @property
    def t(self):
        return self._t

    @property
    def f(self):
        return self._f

    @property
    def cost(self):
        return self._cost


INF = 1 << 28


# ここから本実装
def bellman_ford(n: int, edges, s: int):
    dist = [INF for _ in range(n)]
    dist[s] = 0

    for i in range(2 * n):
        for e in edges:

            if dist[e.t] > dist[e.f] + e.cost:
                dist[e.t] = dist[e.f] + e.cost
                if i >= n - 1:
                    return None

    return dist
