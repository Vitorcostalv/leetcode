MOD = 10**9 + 7

class Solution(object):
    def waysToFillArray(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        max_n = 10000
        
        fact = [1] * (max_n + 1)
        for i in range(2, max_n + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        inv_fact = [1] * (max_n + 1)
        inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
        for i in range(max_n - 1, 0, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
        
        def nCr(n, r):
            if n < r:
                return 0
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD
        
        def prime_factorization(n):
            factors = {}
            d = 2
            while d * d <= n:
                while (n % d) == 0:
                    if d not in factors:
                        factors[d] = 0
                    factors[d] += 1
                    n //= d
                d += 1
            if n > 1:
                factors[n] = 1
            return factors
        
        results = []
        for n, k in queries:
            if k == 1:
                results.append(1)
                continue
            
            factors = prime_factorization(k)
            ways = 1
            for _, exp in factors.items():
                ways = ways * nCr(n + exp - 1, exp) % MOD
            results.append(ways)
        
        return results
