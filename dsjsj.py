import sys

def main():
    data = sys.stdin.read().split()
    A, B, C = map(float, data[:3])  # x0, y0, z0 are not needed

    nn = A*A + B*B + C*C
    s = A + B + C
    det = 3*nn - s*s  # > 0 since A, B, C are not all equal

    print("%.8f" % (nn / det))

main()