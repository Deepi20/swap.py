import math
import os
import random
import re
import sys


def countSwaps(a):
    count = 0
for i in range(len(a)):
    for j in range(len(a)-1):
            if (a[j] > a[j + 1]):
                s = a[j]
                a[j] = a[j+1]
                a[j + 1] = s
                count += 1
        print "Array is sorted in",str(count),"swaps."
        print "First Element:",a[0]
        print "Last Element:",a[-1]

if __name__ == '__main__':
    n = int(raw_input())

    a = map(int, raw_input().rstrip().split())

    countSwaps(a)
