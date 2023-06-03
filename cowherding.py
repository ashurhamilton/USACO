x = int(input())
y = int(input())
z = int(input())

unsorted = []
unsorted.append(x)
unsorted.append(y)
unsorted.append(z)

sorted = unsorted.sort()

a = sorted[1] - sorted[0]
b = sorted[2] - sorted[1]

if a<=b:
    if a<=2:
        min = 1
    else:
        min = 2
elif b>a:
    if b<=2:
        min = 1
    else:
        min = 2