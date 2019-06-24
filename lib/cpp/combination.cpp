#include <iostream>
using namespace std;

const long long MOD = 1000000007;
long long fac[200001];

void init() {
  fac[0] = fac[1] = 1;
  for (int i = 2; i < 200001; i++) {
    fac[i] = fac[i - 1] * i % MOD;
  }
}

// a^n mod を計算する
long long modpow(long long a, long long n) {
  long long res = 1;
  while (n > 0) {
    if (n & 1) {
      res = res * a % MOD;
    }
    a = a * a % MOD;
    n >>= 1;
  }
  return res;
}

// a^{-1} mod を計算する
long long modinv(long long a) { return modpow(a, MOD - 2); }

long long nCk(long long n, long long k) {
  if (n < k) {
    return 0;
  }
  if (n < 0 || k < 0) {
    return 0;
  }
  return fac[n] * (modinv(fac[k]) * modinv(fac[n - k]) % MOD) % MOD;
}
