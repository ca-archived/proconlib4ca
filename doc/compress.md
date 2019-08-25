---
layout: algorithm
langs:
  - name: python
    code_path: python/compress.py
    verify_by: nyama
    verify_at: -
    verify_url: -
---

# 解説

- 配列の要素を、大小関係を保ったまま要素を圧縮する
- [1, 5, 10] -> [0, 1, 2] というような感じ

# 計算量

要素数 _N_ = DisjointSet.size に対して O(_α_(_N_ log _N_))
