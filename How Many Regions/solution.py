import bisect
from collections import deque
import sys


def input():
    return sys.stdin.readline()
def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))

w, h, n = inp(), inp(), inp()
x1, x2, y1, y2 = inlt(), inlt(), inlt(), inlt()

def compress(x1, x2 , w):
    print("to compress {} {}".format(x1, x2))
    xs = []
    for i in range(n):
        for d in range(-1, 2):
            tx1, tx2 = x1[i] + d, x2[i] + d
            if 1 <= tx1 <= w:
                xs.append(tx1)
                print("push x1 {}".format(tx1))
            if 1 <= tx2 <= w:
                xs.append(tx2)
                print("push x2 {}".format(tx2))
    
    xs.sort()
    print("got xs {}".format(xs))
    xs = list(set(xs))
    print("remove duplicated got xs {}".format(xs))
    for i in range(n):
        newValue = bisect.bisect_left(xs, x1[i]) - 0
        print("assgin x1[{}] from old value {} to new value {}".format(i, x1[i], newValue))
        x1[i] = newValue
        newValue = bisect.bisect_left(xs, x2[i]) - 0
        print("assgin x2[{}] from old value {} to new value {}".format(i, x2[i], newValue))
        x2[i] = newValue
    return len(xs)

w = compress(x1, x2, w)
h = compress(y1, y2, h)
fld = [[False] * (n * 6) for _ in range(n * 6)]
for i in range(n):
    for y in range(y1[i], y2[i] + 1):
        for x in range(x1[i], x2[i] + 1):
            fld[y][x] = True

ans = 0
for y in range(h):
    for x in range(w):
        if fld[y][x]:
            continue
        ans += 1
        print("find {} {} unique area".format(y,x))
        que = deque()
        que.append((x, y))
        while que:
            sx, sy = que.popleft()
            # for i in range(4):
                # tx, ty = sx + dx[i]
            
