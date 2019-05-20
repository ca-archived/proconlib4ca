# 解説

以下のUnion-Findアルゴリズムを使用できるDisjointSet (UnionFind木)データ構造
- same(x, y): xとyが同じ木に属するか判定
- unite(x, y): xが属する木とyが属する木を合併する
- find(x): xが属する木の根を返す

# 計算量

要素数 *N* = DisjointSet.size に対してO(*α*(*N*))

※ *α*(*n*)はアッカーマン関数*A*(*n*, *n*)の逆関数。ならし計算量

# コード

## java

[Template.java](../lib/java/Template.java)

## c++

[template.cpp](../lib/cpp/template.cpp)

# 検証

## java

なし
