from collections import defaultdict
import sys


def input():
    return sys.stdin.readline().rstrip()
def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_end = True
    def search(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if not node:
                return False
        return node.is_end

n = inp()
trie = Trie()

for i in range(n):
    trie.insert(input())

print(trie.search("word"))
print(trie.search("word1"))
