n = int(input())
cows = list(input())
cnt = 0
cnt_g = 0;
cnt_h = 0;

for i in range(len(cows)):
    cnt_g = 0
    cnt_h = 0
    for j in range(i, len(cows)):
        if cows[j] == "G":
            cnt_g += 1
        if cows[j] == "H":
            cnt_h += 1
            # print("no errors up to here")
        if cnt_g == 1 or cnt_h == 1:
            cnt += 1

ans = cnt - (n + n-1)

print(ans)