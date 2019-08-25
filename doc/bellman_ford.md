---
layout: algorithm
langs:
  - name: python
    code_path: python/bellman_ford.py
    verify_by: nyama
    verify_at: AtCoder - abc137_E
    verify_url: https://atcoder.jp/contests/abc137/submissions/6855678
---

# 解説

単一始点最短経路問題を解決可能なアルゴリズム。負辺があっても動作し、負閉路を検出することもできる。
基本方針はワーシャル・フロイド法と一緒だが、辺の分だけループを回し、経路のアップデートをすることを | _E_ | 回行う。 

# 計算量

頂点数: \| _V_ \| 
辺数: \| _E_ \|
として、 O( \| _V_ \| \| _E_ \| )
