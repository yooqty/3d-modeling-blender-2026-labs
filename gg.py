import sys

def main():
    data = sys.stdin.read().split()
    vals = list(map(float, data[:18]))

    a = [[0.0] * 3 for _ in range(3)]
    b = [[0.0] * 3 for _ in range(3)]
    for i in range(3):
        row = vals[i * 6:(i + 1) * 6]
        a[i] = row[:3]
        b[i] = row[3:]

    s = [[a[i][j] + b[i][j] for j in range(3)] for i in range(3)]

    # A_j = столбец j матрицы a, S_i = столбец i матрицы s
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            dot = sum(a[k][j] * s[k][i] for k in range(3))
            if dot > 1e-12:
                print("YES")
                return
    print("NO")

main()