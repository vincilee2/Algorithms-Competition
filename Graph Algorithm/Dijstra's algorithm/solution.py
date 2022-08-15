from collections import defaultdict
import heapq
from math import inf
import sys


def input():
    return sys.stdin.readline()
def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))

# construct dag from input data
m = inp()
n = inp()
dag = defaultdict(list)
for _ in range(n):
    a, b, w = inlt()
    dag[a].append((b,w))
print(dag)
dist = [inf for _ in range(m)]
dist[0] = 0
pq = [(0,0)]

while pq:
    d, u = heapq.heappop(pq)
    if dist[u] < d:
        continue
    for v, w in dag[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))
print(dist)