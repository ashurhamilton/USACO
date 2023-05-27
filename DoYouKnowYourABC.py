numbers = list(map(int, input().split()))
numbers.sort()

a = numbers[0]
b = numbers[1]
c = numbers[-1] - (a+b)

print(a, b, c)