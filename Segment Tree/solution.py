import sys

from numpy import Inf

def input():
    return sys.stdin.readline()
def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))

def init(n):
# the number of segment tree is 2n which n is the number of an array.
    for i in range(2 * n - 1):
        data[i] = Inf

# update the value at k-th index to a
def update(k, a):
    k += n - 1
    data[k] = a
    while k > 0:
        parent_index = (k - 1) / 2
        # data[parent_index] is minimun value of it's two children
        left_child_index = parent_index * 2 + 1
        right_child_index = left_child_index + 1
        winner_value = min(data[left_child_index], data[right_child_index])
        print("update the parent at {} of index {} from {} to {} with it's two children at data[{}]={} and data[{}]={}".format( \
            parent_index, k, data[parent_index], winner_value, left_child_index, data[left_child_index], right_child_index, data[right_child_index]))
        data[parent_index] = winner_value
        k = parent_index
# query the minimum value of interval [a,b)
# external usage:
# query(a,b,0,0,n)
def query(a, b, k, l, r):
    if r <= a or b <= l:
        print("inteval[{},{}) not interleave with interval[{},{})".format(a,b,l,r))
        return Inf
    if a <= l and r <= b:
        print("inteval[{},{}) is included in interval[{},{}) so return value data[{}] = {}".format(\
            l,r,a,b,k,data[k]))
        return data[k]
    else:
        vl = query(a, b, k * 2 + 1, l, (l + r) // 2)
        print("the minimum of left part[{},{}) is {}".format(\
            l, (l + r) // 2, vl))
        vr = query(a, b, k * 2 + 2, (l + r) // 2, r)
        print("the minimum of left part[{},{}) is {}".format(\
            (l + r) // 2, r, vr))
        return min(vl, vr)

n = inp()

data = [0] * (2 * n - 1)

init(n)

data_raw = inlt()

print("original array is {}".format(data_raw))
for i, a in enumerate(data_raw):
    update(i, a)

print("segment tree is {}".format(data))