import sys

from numpy import Inf


def input():
    return sys.stdin.readline()
def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))

nums = inlt()

n = len(nums)

minLeft, maxLeft = [0] * n, [0] * n
minStack, maxStack = [], []

for i, num in enumerate(nums):
    while minStack and nums[minStack[-1]]  > num:
        print("nums[{}] = {} is greater than nums[{}] = {} so pop it".format(  
        minStack[-1], nums[minStack.pop()], i, num))
    minLeft[i] = minStack[-1] if minStack else -1
    assignNum = nums[minStack[-1]] if minStack else -Inf
    print("assign {} to minLeft[{}], so nums[{}] = {} is the left latest number lower than nums[{}] = {}".format( \
          minLeft[i], i, minLeft[i], assignNum, i, num))
    print("from {} to {} all number is no more than nums[{}] = {}".format( \
          minLeft[i] + 1, i, i, num))
    minStack.append(i)
    
    while maxStack and nums[maxStack[-1]] < num:
        print("{} is less than nums[{}] = {} so pop it".format(nums[maxStack.pop()], i, num))
    maxLeft[i] = maxStack[-1] if maxStack else -1
    assignNum = nums[maxStack[-1]] if maxStack else Inf
    print("assign {} to maxLeft[{}], so nums[{}] = {} is the left latest number larger than nums[{}] = {}".format( \
          maxLeft[i], i, maxLeft[i], assignNum, i, num))
    print("from {} to {} all number is no less than nums[{}] = {}".format( \
          maxLeft[i] + 1, i, i, num))      
    maxStack.append(i)

