import sys

def main():
    data = sys.stdin.read().replace(",", ".").split()
    A, B, C = float(data[0]), float(data[1]), float(data[2])

    nn = A*A + B*B + C*C
    det = (A - B)**2 + (B - C)**2 + (C - A)**2  # = 3*nn - (A+B+C)^2

    if det < 1e-12:
        # A = B = C: no valid (a, b, c) exists
        print("0.00000000")
        return

    print("%.8f" % (nn / det))

main()