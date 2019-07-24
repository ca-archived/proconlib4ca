---
layout: algorithm
langs:
  - name: python
    code_path: python/dijkstra.py
    verify_by: nyama
    verify_at: AtCoder - abc035 D
    verify_url: https://atcoder.jp/contests/abc035/submissions/6235729
---


# 解説

グラフ上の２頂点間の最短経路を求めるアルゴリズム。
隣接行列で実装するパタンと隣接リストで実装するパタンの2種類がある。
ここでは隣接リストによる実装を示す。

# 計算量

グラフの頂点数を N 、辺数を M として O((N + M) logN)
