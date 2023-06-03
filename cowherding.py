x = int(input())
y = int(input())
z = int(input())

sorted = []
sorted.append(x)
sorted.append(y)
sorted.append(z)
sorted.sort()
a = sorted[1] - sorted[0]
b = sorted[2] - sorted[1]
print(a, b)
if a<=b:
    if a<=2:
        small = 1
    else:
        small = 2
else:
    if b<=2:
        small = 1
    else:
        small = 2

if a>=b:
    large = a-1
if b>a:
    large = b-1

print(small)
print(large)