import math

with open("pails.in") as file:
	x, y, m = map(int, file.readline().split())


file.close()
milk_left = 0
min = 1000

for i in range(math.floor(m/y)):
    milk_left = (m - (i*y)) % x
    if(milk_left < min):
        min = milk_left

total_milk = m - min

file = open("pails.out", "w")
file.write(str(total_milk))
file.close()