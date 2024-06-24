import math

N = int(input())
places = list(input())
passed_to = []
cnt = 0

def target(x):
    left_num = 0
    distance_left = 1000
    right_num = 0
    distance_right = 1000
    for i in range(N):
        if(places[i] < places[x] and places[x] - places[i] < distance_left):
            left_num = i
            distance_left = places[x] - places[i]
        elif(places[i] > places[x] and places[i] - places[x] < distance_right):
            right_num = i
            distance_right = places[i] - places[x]
    
    if(distance_right < distance_left):
        return right_num
    else:
        return left_num


for i in range(N):
    target(places[i]).append(passed_to)

for i in range(N):
    if(places[i] not in passed_to):
        cnt += 1






if N == 1 or N == 2:
    print(1)





