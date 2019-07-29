public class UnionFind {
    int[] parents, sizes;

    UnionFind(int n) {
        parents = new int[n];
        sizes = new int[n];
        for(int i = 0; i < n; i++) {
            parents[i] = i;
            sizes[i] = 1;
        }
    }

    public int find(int x) {
        if (x == parents[x]) return x;
        return parents[x] = find(parents[x]);
    }

    public void unite(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) return;
        if (sizes[x] < sizes[y]) {
            int temp = x;
            x = y;
            y = temp;
        }
        parents[y] = x;
        sizes[x] += sizes[y];
    }

    public boolean same(int x, int y) {
        return find(x) == find(y);
    }

    public int size(int x) {
        return sizes[find(x)];
    }

}
