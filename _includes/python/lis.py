from bisect import bisect_right


def lis(ar):
    """
    最長増加列長を求める(O(N logN)
    :param ar: 最長増加列を求めたい配列
    :return: 最大増加列長, 辞書順最小の最長増加列
    """
    n = len(ar)
    dir = [-1] * n
    dir[0] = 0

    inc_ar = []
    inc_ar.append(ar[0])

    size = 1
    for i in range(1, n):
        x = ar[i]
        if inc_ar[size - 1] < x:
            inc_ar.append(x)
            size += 1
            dir[i] = size - 1
        else:
            r = bisect_right(inc_ar, x, 0, size)
            inc_ar[r] = x
            dir[i] = r

    red = size - 1
    path = []
    for rev in range(n):
        i = n - rev - 1
        if dir[i] == red:
            path.append(ar[i])
            red -= 1

    for i in range(size // 2):
        rev = size - i - 1
        path[i], path[rev] = path[rev], path[i]

    return size, path
