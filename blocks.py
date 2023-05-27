import sys
from collections import Counter

N = int(input())
blocks = []
for i in range(4):
    blocks.append(set(input()))

def var():
    x = input().strip()
    k = Counter(x)


counter = 0

for a in blocks[0]:
        for b in blocks[1]:
            for c in blocks[2]:
                for d in blocks[3]:
                    y = Counter([a, b, c, d])

                    for i in k:
                        if y[i] < [i]:
                            break
                    else:
                        print("YES")
print("NO")
                
for j in range(N):
    var()