# 解説

以下の Union-Find アルゴリズムを使用できる DisjointSet (UnionFind 木)データ構造

- same(x, y): x と y が同じ木に属するか判定
- unite(x, y): x が属する木と y が属する木を合併する
- find(x): x が属する木の根を返す

# 計算量

要素数 _N_ = DisjointSet.size に対して O(_α_(_N_))

※ _α_(_n_)はアッカーマン関数*A*(_n_, _n_)の逆関数。ならし計算量

# コード

## java

なし

## c++

[union_find.cpp](../lib/cpp/union_find.cpp)

## python

[union_find.py](../lib/python/union_find.py)

# 検証

## java

なし

## c++

[AtCoder - abc097 D](https://atcoder.jp/contests/abc097/submissions/5489399)

## python

[AtCoder - abc126 E](https://atcoder.jp/contests/abc126/submissions/5488956)
