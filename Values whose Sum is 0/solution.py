import bisect
import sys


def input():
    return sys.stdin.readline()
def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))

n = inp()
A, B, C, D = inlt(), inlt(), inlt(), inlt()

CD = [0] * (n * n)
for i in range(n):
    for j in range(n):
        CD[i * n + j] = C[i] + D[j]
CD.sort()
print("C D combinations: {}".format(CD))
res = 0
for i in range(n):
    for j in range(n):
        cd = -(A[i] + B[j])
        left = bisect.bisect_left(CD, cd)
        right = bisect.bisect_right(CD, cd)
        if right - left > 0:
            print("find {} in A and {} in B match {} in CD".format(A[i], B[j], cd))
        res += (right - left)
print(res)
