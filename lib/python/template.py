# 参考: https://qiita.com/y-tsutsu/items/aa7e8e809d6ac167d6a1

import sys
import heapq, math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy

# 多次元配列
# dp = [[0] * 3 for _ in range(5)]

# 入力を受け取る
n, m = map(int, input().split())

# 出力
print(*[1, 2, 3], sys.stderr)  # プリントでバッグならエラー出力にしておくと、atcoder提出時も無視される
print(*[1, 2, 3])
# >> 1 2 3
