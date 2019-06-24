class Combination:
    def __init__(self, N: int, MOD: int):
        fac = [0 for _ in range(N + 1)]
        fac[0] = 1
        for i in range(1, N + 1):
            fac[i] = fac[i - 1] * i % MOD
        self.fac = fac
        self.N = N
        self.MOD = MOD

    def _modpow(self, x: int, n: int) -> int:
        ret = 1
        while n > 0:
            if n % 2 == 1:
                ret = ret * x % self.MOD
            x = x * x % self.MOD
            n >>= 1
        return ret

    def _modinv(self, x: int) -> int:
        return self._modpow(x, self.MOD - 2)

    def combination(self, n: int, k: int) -> int:
        return self.fac[n] * self._modinv(self.fac[k]) % self.MOD * self._modinv(self.fac[n - k]) % self.MOD
