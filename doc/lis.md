---
layout: algorithm
langs:
  - name: python
    code_path: python/lis.py
    verify_by: nyama
    verify_at: AtCoder - abc006_D
    verify_url: https://atcoder.jp/contests/abc006/submissions/6544339
---

# 解説

配列arが与えられたとき、効率的に最長増加列(LIS: Longest Increasing Subsequence)を求めるアルゴリズム。
inc_ar[idx]: 長さidxの増加列を構築するとき、idx番目に登録される最小の数値。
入力の配列を左から見ていき、その数値xを挿入できるidxを二分探索で求め、inc_ar[idx]をxで置き換える。
これを全て完了したときのinc_arの長さが求める最長増加列の最大長である。
経路復元する場合、配列の各要素について、その要素が挿入された位置をメモしておく。
このメモを右からいき、各idxについて最初に見つかったものを使って構成すれば良い。

# 計算量

配列の要素をみるのに O(N) 、二分探索に O(log N) なので、合わせて O(N log N)
