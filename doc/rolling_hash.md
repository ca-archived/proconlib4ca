---
layout: algorithm
langs:
  - name: python
    code_path: python/rolling_hash.py
    verify_by: nyama
    verify_at: AtCoder - abc141 E
    verify_url: https://atcoder.jp/contests/abc141/submissions/7574786
---

# 解説

文章Sをハッシュ化し、部分文字列 `[l, r)` のハッシュ値を計算可能なアルゴリズム。
部分文字列の包含判定などを高速に行うことができる

# 計算量

O(\|S\|)
