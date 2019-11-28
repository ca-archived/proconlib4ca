---
layout: algorithm
langs:
  - name: java
    code_path: java/BinarySearch.java
    verify_by: ryochanuedasan
    verify_at: AtCoder - abc077_C
    verify_url: https://atcoder.jp/contests/abc077/submissions/5086235
---

# 解説

二分探索
ソート済み*array*に対して*value*を検索する

# 計算量

*array*の要素数 _N = |array|_ に対して
O(logN)

# 使用例

```
array = [0, 1, 1, 3, 4, 4, 6] に対し、

lowerBound(array, -1): 0
lowerBound(array, 1): 1
lowerBound(array, 2): 3
lowerBound(array, 7): 7
=========================
upperBound(array, 7): 7
upperBound(array, 4): 6
upperBound(array, 2): 3
upperBound(array, -1): 0
```
