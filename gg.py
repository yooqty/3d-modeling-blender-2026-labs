import sys

def main():
    vals = list(map(float, sys.stdin.read().split()))
    a = [vals[i*6:i*6+3] for i in range(3)]
    b = [vals[i*6+3:i*6+6] for i in range(3)]
    s = [[a[i][j] + b[i][j] for j in range(3)] for i in range(3)]

    # обратная матрица s через алгебраические дополнения
    def minor(m, r, c):
        rows = [k for k in range(3) if k != r]
        cols = [k for k in range(3) if k != c]
        return (m[rows[0]][cols[0]] * m[rows[1]][cols[1]]
                - m[rows[0]][cols[1]] * m[rows[1]][cols[0]])

    det = sum(s[0][j] * ((-1) ** j) * minor(s, 0, j) for j in range(3))
    inv = [[((-1) ** (i + j)) * minor(s, j, i) / det for j in range(3)]
           for i in range(3)]

    # M[j][i] = A_j · q_i, где q_i = i-й столбец s^{-1}
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            dot = sum(a[k][j] * inv[k][i] for k in range(3))
            if dot > 1e-9:
                print("YES")
                return
    print("NO")

main()