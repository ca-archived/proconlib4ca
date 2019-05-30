
import sys
# 多次元配列
# dp = [[0] * 3 for _ in range(5)]

# 入力を受け取る
n, m = map(int, input().split())


# 出力
print(*[1, 2, 3], sys.stderr) # プリントでバッグならエラー出力にしておくと、atcoder提出時も無視される
print(*[1, 2, 3])
# >> 1 2 3
