import sys

from numpy import Inf

def input():
    return sys.stdin.readline()
def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))

n = input()

data = [0] * n

def init(n):
    ni = 1
    while ni < n:
        n *= 2
    for i in range(2 * ni - 1):
        data[i] = - Inf

def update(k, a):
    k += n - 1
    data[k] = a
    