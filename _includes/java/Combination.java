public class Combination {
    int n;
    long mod;
    long[] facts;

    public Combination(int n, long mod) {
        this.n = n;
        this.mod = mod;
        facts = new long[n];
        facts[0] = 1;
        for (int i = 1; i < n; i++) {
            facts[i] = facts[i - 1] * i % mod;
        }
    }

    long modpow(long a, long b) {
        if (b == 0) return 1;
        else if (b == 1) return a;

        long x = modpow(a, b / 2);
        return b % 2 == 0 ? x * x % mod : x * (x * a % mod) % mod;
    }

    long inv(long n) {
        return modpow(n, mod - 2);
    }

    public long nck(int n, int k) {
        return n < k ? 0 : facts[n] * (inv(facts[n - k]) * inv(facts[k]) % mod) % mod;
    }
}
