import sys

def input():
    return sys.stdin.readline()
def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))

dirs_str = input()

N = len(dirs_str)

dir = [0 if dir == 'F' else 1 for dir in dirs_str]


def calc(K):
    f = [0] * N
    i, res, sum = 0, 0, 0
    while i + K <= N:
        if (dir[i] + sum) % 2 != 0:
            res += 1
            f[i] = 1
        sum += f[i]
        if (i - K + 1) >= 0:
            sum -= f[i - K + 1]
        i += 1
    for i in range(N - K + 1, N):
        if (dir[i] + sum) % 2 != 0:
            return -1
        if i - K + 1 >= 0:
            sum -= f[i - K + 1]
    return res

K ,M = 1, N
for k in range(1, N + 1):
    m = calc(k)
    if m >= 0 and M > m:
        M = m
        K = k
print(K, M)

