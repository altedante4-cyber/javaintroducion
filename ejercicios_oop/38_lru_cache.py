from functools import lru_cache

class Fibonacci:
    @staticmethod
    @lru_cache(maxsize=None)
    def calcular(n):
        if n <= 1:
            return n
        return Fibonacci.calcular(n - 1) + Fibonacci.calcular(n - 2)

print("=== Fibonacci con memoization ===")
for i in range(15):
    print(f"F({i}) = {Fibonacci.calcular(i)}")
