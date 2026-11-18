import sys

def main():
    data = sys.stdin.read().split()
    a = data[0]
    n = len(a)
    m = int(data[1])
    tbl = str.maketrans("+-", "01")

    # Distinct orthants as integers (first character = highest bit)
    rows = set(int(s.translate(tbl), 2) for s in data[2:2 + m])

    # A nonempty monomial is positive in exactly half of the orthants.
    # The constant 1 would be positive everywhere, but m < 2^n.
    if len(rows) != 1 << (n - 1):
        print("NO")
        return

    # Gaussian elimination over GF(2): we look for S such that
    # for every row x, parity(x & S) == 0
    basis = {}  # pivot bit -> row (kept fully reduced)
    for x in rows:
        if len(basis) == n - 1:
            break
        for p, b in basis.items():
            if (x >> p) & 1:
                x ^= b
        if x:
            p = x.bit_length() - 1
            for q in basis:
                if (basis[q] >> p) & 1:
                    basis[q] ^= x
            basis[p] = x

    if len(basis) != n - 1:
        print("NO")
        return

    # Find the free column and build the solution vector S
    free = next(i for i in range(n) if i not in basis)
    S = 1 << free
    for p, b in basis.items():
        if (b >> free) & 1:
            S |= 1 << p

    # Verify all orthants
    for x in rows:
        if bin(x & S).count("1") & 1:
            print("NO")
            return

    # Bit n-1-i corresponds to the i-th letter
    res = [a[i] for i in range(n) if (S >> (n - 1 - i)) & 1]
    print("".join(res))

main()