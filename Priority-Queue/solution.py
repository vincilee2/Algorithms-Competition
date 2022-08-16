import sys

def input():
    return sys.stdin.readline()
def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))

p = inlt()

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def push(self, item):
        k = self.size
        self.queue.append(item)
        self.up(k, item)
        self.size += 1

    def up(self, k, item):
        print("k = {}, up value = {}".format(k, item))
        while k > 0:
            p = (k - 1) >> 1  # k - 1 important
            pv = self.queue[p]
            print("p = {}, pv = {}".format(p, pv))
            if pv <= item:
                print("break since parent node value = {} <= up value = {}".format(pv, item))
                break
            print("move parent at {} with value {} down to {}".format(p, pv, k))
            self.queue[k] = pv
            k = p
        self.queue[k] = item
    
    def pop(self):
        if self.size == 0:
            return None
        item = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop()
        self.size -= 1
        if (self.size > 0):
            self.down(0)
        return item
    def down(self, k):
        half = self.size >> 1
        item = self.queue[k]
        print("down from {} with value {}".format(k, item))
        while k < half:
            c = k << 1
            right = c + 1
            cv = self.queue[c]
            if right < self.size and self.queue[right] < cv:
                c = right
                cv = self.queue[right]
            if cv >= item:
                break
            print("move child at {} with value {} up to {}".format(c, cv, k))
            self.queue[k] = cv
            k = c
        self.queue[k] = item

pq = PriorityQueue()
for i in p:
    pq.push(i)
print(pq.queue)
n = len(pq.queue)

print("pop from priority queue")
print([ pq.pop() for i in range(n)])

