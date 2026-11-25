import sys
forb = set()
for line in sys.stdin.read().split("\n"):
    s = "".join(line.split())
    if len(s) >= 2:
        forb.add(s[0] + s[1])
        forb.add(s[1] + s[0])
ok = [t for t in "xyz" if t + t not in forb]
print("YES" if ok else "NO")