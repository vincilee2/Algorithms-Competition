import sys


def input():
    return sys.stdin.readline()
def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))

# construct dag from input data
n = inp()
dag = [{} for _ in range(n)]
for _ in range(n - 1):
    a, b, w = inlt()
    dag[a].append((b - 1))