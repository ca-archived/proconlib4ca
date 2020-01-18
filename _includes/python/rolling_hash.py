

class RollingHash:

    PS1 = 1009
    PS2 = 1007
    PL1 = 100000007
    PL2 = 100000009

    def __init__(self, s: str):
        self._n = len(s) + 1
        self._pow1, self._pow2, self._hash1, self._hash2 = self._initialize(s, self._n)

    def _initialize(self, s: str, n: int):
        pow1 = [1 for _ in range(n)]
        pow2 = [1 for _ in range(n)]
        hash1 = [0 for _ in range(n)]
        hash2 = [0 for _ in range(n)]

        idx = 1
        for c in s:
            pow1[idx] = pow1[idx - 1] * self.PS1 % self.PL1
            pow2[idx] = pow2[idx - 1] * self.PS2 % self.PL2
            hash1[idx] = (hash1[idx - 1] * self.PS1 + ord(c) - ord('a') + 1) % self.PL1
            hash2[idx] = (hash2[idx - 1] * self.PS2 + ord(c) - ord('a') + 1) % self.PL2
            idx += 1

        return pow1, pow2, hash1, hash2

    def get(self, l: int, r: int):
        p1 = ((self._hash1[r] - self._hash1[l] * self._pow1[r - l]) % self.PL1 + self.PL1) % self.PL1
        p2 = ((self._hash2[r] - self._hash2[l] * self._pow2[r - l]) % self.PL2 + self.PL2) % self.PL2
        return p1, p2
