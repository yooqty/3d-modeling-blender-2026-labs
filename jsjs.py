import sys

def jacobi_eigenvalues(M, n):
    a = [row[:] for row in M]
    for _ in range(100):
        # largest off-diagonal element
        p = q = 0
        mx = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > mx:
                    mx = abs(a[i][j])
                    p, q = i, j
        if mx < 1e-12:
            break
        theta = (a[q][q] - a[p][p]) / (2.0 * a[p][q])
        if theta >= 0:
            t = 1.0 / (theta + (1.0 + theta * theta) ** 0.5)
        else:
            t = -1.0 / (-theta + (1.0 + theta * theta) ** 0.5)
        c = 1.0 / (1.0 + t * t) ** 0.5
        s = t * c
        for k in range(n):
            akp, akq = a[k][p], a[k][q]
            a[k][p] = c * akp - s * akq
            a[k][q] = s * akp + c * akq
        for k in range(n):
            apk, aqk = a[p][k], a[q][k]
            a[p][k] = c * apk - s * aqk
            a[q][k] = s * apk + c * aqk
    return sorted(a[i][i] for i in range(n))

def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    edges = []
    for i in range(m):
        u = int(data[2 + 2 * i]) - 1
        v = int(data[3 + 2 * i]) - 1
        edges.append((u, v))

    best = None
    for skip in range(m):
        L = [[0.0] * n for _ in range(n)]
        for idx, (u, v) in enumerate(edges):
            if idx == skip:
                continue
            L[u][u] += 1
            L[v][v] += 1
            L[u][v] -= 1
            L[v][u] -= 1
        if n == 1:
            lam2 = 0.0
        else:
            ev = jacobi_eigenvalues(L, n)
            lam2 = ev[1]
        if lam2 < 0:
            lam2 = 0.0
        if best is None or lam2 < best:
            best = lam2

    if best < 5e-10:
        best = 0.0
    print("%.3f" % best)

main()