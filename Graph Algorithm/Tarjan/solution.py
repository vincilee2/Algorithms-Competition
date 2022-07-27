from collections import defaultdict
import sys


def input():
    return sys.stdin.readline()
def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))

# construct dag from input data
n = inp()
dag = defaultdict(list)
for _ in range(n):
    u, v = inlt()
    dag[u].append(v)
    # dag[v].append(u)

stackMember = defaultdict(bool)
low = defaultdict(int) # 
disc = defaultdict(int)
stack = []
def tarjan(time, u):
    print("time now:", time)
    time += 1
    disc[u] = low[u] = time
    stackMember[u] = True
    stack.append(u)
    print('visit adj of {u} : {adj}:'.format(u=u, adj = dag[u]))
    for v in dag[u]:
        if disc[v] == 0:
            print("node {v} is not visited".format(v=v))
            tarjan(time, v)
            low[u] = min(low[u], low[v])
        elif stackMember[v]:
            print("node {v} is in stack".format(v=v))
            if (disc[v] < low[u]):
                print("node {v} is earlier than any node that could reach to {u}, so set low[{u}] = {discV}".format(v=v, u = u, discV = disc[v]))
                low[u] = disc[v]
            low[u] = min(low[u], disc[v])
    w = -1
    if low[u] == disc[u]:
        print("node {u} is a root".format(u=u))
        while w != u:
            w = stack.pop()
            stackMember[w] = False
            print("pop {w} from stack".format(w=w))
        print()
tarjan(0, 0)