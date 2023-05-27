import sys

N = int(input())
numbers = list(map(int, input().split()))
total = 0
chain_sum = 0

for i in range(len(numbers)):
    chain_sum = 0
    for j in range(i, len(numbers)):
        chain_sum += numbers[j] #FINDS TOTAL
        chain_avg = (chain_sum) / (j-i+1)
        if chain_sum % (j - i + 1) == 0:
            if chain_avg in numbers[i:j+1]:
                    total += 1

sys.stdout.write(str(total))




