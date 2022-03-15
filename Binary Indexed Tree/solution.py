import sys


def input():
    return sys.stdin.readline()
def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))

# Returns sum of arr[0..index]
def sum(tree, i):
    s = 0
    print("to get sum of arr[0..{}]".format(i))
    i = i + 1
    while i > 0:
        print("add current element tree[{}] = {} to sum {} get {}".format(\
            i, tree[i], s, s + tree[i]))
        s += tree[i]
        print("move index from {0:b} to parent {1:b}".format(\
            i, i - i & (-i)))
        i -= i & (-i)
    return s

def update(tree, n, i, v):
    i += 1
    print("update value {} from arr[{}]".format(v, i))
    while i <= n:
        print("add value {} to tree[{}] = {} get {}".format(\
            v, i, tree[i], v + tree[i]))
        tree[i] += v
        print("update index from {0:b} to view parent {1:b}".format(\
            i, i + i & (-i)))
        i += i & (-i)
        print("current tree is :")
        plot(tree, n)

        
def construct(arr, n):
    tree = [0] * (n + 1)

    for i in range(n):
        update(tree, n, i, arr[i])

    return tree


def plot(tree, n):
    plot_levels = [""] * (n.bit_length())
    for i in range(1, n + 1):
        last_bit = i & (-i)
        level = "{0:b}".format(last_bit).count('0')
        # print("last_bit {0:b} count 0 {1}".format(last_bit, level))
        placeholder = ""
        if plot_levels[level] != "":
            for j in range(level + 1):
                placeholder += ' ' * 6
        for j in range(1 << (level + 1)):
            placeholder += '-' * 3
        
        placeholder = list(placeholder)
        num = "{0:b}:{1}".format(i, tree[i])
        placeholder[-len(num):] = list(num)
        
        plot_levels[level] += ''.join(placeholder)

    for i in range(len(plot_levels) - 1, -1, -1):
        print(plot_levels[i])


arr = inlt()
n = len(arr)
tree = construct(arr, n)
