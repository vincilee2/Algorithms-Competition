from cmath import sqrt
import sys
g = 10.0

def input():
    return sys.stdin.readline()
def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))

N = inp()
H = inp()
R = inp()
T = inp()

def calc(T):
    if T < 0:
        return H
    t = abs(sqrt(2 * H / g))
    k = int(T / t)
    if k % 2 == 0:
        d = T - k * t
        return H - g * d * d / 2
    else:
        d = k * t + t - T
        return H - g * d * d / 2
y = [0] * N
for i in range(N):
    y[i] = calc(T - i)
y.sort()
for i in range(N):
    print(y[i] + 2 * R * i / 100.0)