---
layout: algorithm
langs:
  - name: java
    code_path: java/Combination.java
    verify_by: ryochanuedasan
    verify_at: AtCoder - abc034_C
    verify_url: https://atcoder.jp/contests/abc034/submissions/6105978
  - name: cpp
    code_path: cpp/combination.cpp
    verify_by: muras
    verify_at: AtCoder - abc034_C
    verify_url: https://abc034.contest.atcoder.jp/submissions/6095811
  - name: python
    code_path: python/combination.py
    verify_by: nyama
    verify_at: AtCoder - abc034_C
    verify_url: https://atcoder.jp/contests/abc034/submissions/6105635
---

# 解説

フェルマーの小定理を利用して、`nCk mod p` を高速に求めるアルゴリズム。

# 計算量

前計算 O(n)、nCk の計算 O(log p)。
ただし p は素数。
