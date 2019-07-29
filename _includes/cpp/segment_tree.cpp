#include <algorithm>
using namespace std;
typedef long long ll;

const int INF = 2147483647;
const int MAX_N = 1 << 17;

// セグメント木を持つグローバル配列
int n;
int dat[2 * MAX_N - 1];

// 初期化
void init(int n_) {
  n = 1;
  while (n < n_) {
    n *= 2;
  }

  for (int i = 0; i < 2 * n - 1; i++) {
    dat[i] = INF;
  }
}

// k番目の値 (0-indexed) をaに変更
void update(int k, int a) {
  k += n - 1;
  dat[k] = a;

  while (k > 0) {
    k = (k - 1) / 2;
    dat[k] = min(dat[k * 2 + 1], dat[k * 2 + 2]);
  }
}

int inner_query(int a, int b, int k, int l, int r) {
  if (r <= a || b <= l) {
    return INF;
  }

  if (a <= l && r <= b) {
    return dat[k];
  } else {
    int vl = inner_query(a, b, k * 2 + 1, l, (l + r) / 2);
    int vr = inner_query(a, b, k * 2 + 2, (l + r) / 2, r);
    return min(vl, vr);
  }
}

// [a, b) の最小値を求める
int query(int a, int b) { return inner_query(a, b, 0, 0, n); }
