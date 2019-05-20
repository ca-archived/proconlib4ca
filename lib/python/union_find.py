class UnionFind:

    def __init__(self, n: int):
        self._n = n
        self._parents = [i for i in range(n)]
        self._rank = [1 for _ in range(n)]

    def unite(self, x: int, y: int) -> None:
        px = self.find(x)
        py = self.find(y)

        # 一致していないときはリンクをつける
        if px != py:
            self._link(px, py)

    def _link(self, x: int, y: int):
        if self._rank[x] < self._rank[y]:
            self._parents[x] = y
        elif self._rank[x] > self._rank[y]:
            self._parents[y] = x
        else:
            self._parents[x] = y
            self._rank[y] += 1

    def same(self, x: int, y: int) -> bool:
        px = self.find(x)
        py = self.find(y)
        return px == py

    def find(self, x: int) -> int:
        if self._parents[x] == x:
            return x

        self._parents[x] = self.find(self._parents[x])
        return self._parents[x]



n, m = map(int, input().split())

uf = UnionFind(n)

for _ in range(m):
    x, y, _ = map(int, input().split())
    uf.unite(x - 1, y - 1)

s = set()
for i in range(0, n):
    s.add(uf.find(i))

print(len(s))
