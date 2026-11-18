import sys
from functools import lru_cache

def main():
    n, k = map(int, sys.stdin.read().split())

    # state: sorted tuple of remaining column sums (column order doesn't matter)
    @lru_cache(maxsize=None)
    def f(state, rows_left):
        if rows_left == 1:
            # the last row is forced: sum of the remaining column sums equals K
            return 1
        total = 0
        cur = [0] * n

        def dfs(j, left):
            nonlocal total
            if j == n:
                if left == 0:
                    new = tuple(sorted(state[i] - cur[i] for i in range(n)))
                    total += f(new, rows_left - 1)
                return
            # the remaining columns must be able to absorb `left`
            for x in range(min(state[j], left) + 1):
                cur[j] = x
                dfs(j + 1, left - x)
            cur[j] = 0

        dfs(0, k)
        return total

    print(f(tuple([k] * n), n))

main()