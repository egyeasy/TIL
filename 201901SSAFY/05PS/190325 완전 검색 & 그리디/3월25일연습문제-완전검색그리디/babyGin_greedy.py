import time

#arr = [1,2,4,7,8,3]
#arr = [6, 6, 7, 7, 6, 7];
#arr = [0, 5, 4, 0, 6, 0];
#arr = [1, 0, 1, 1, 2, 3];
arr = [7, 8, 9, 9, 0, 1];

stime = time.time()

cnt = [0]*12
for i in range(len(arr)):
    cnt[arr[i]] += 1
    if arr[i] % 10 < 3:
        cnt[arr[i] + 10] += 1

run = triplet = 0
i=0
while i < len(cnt):
    if cnt[i] > 0 and cnt[i+1] > 0 and cnt[i+2] > 0:
        run += 1
        cnt[i] -= 1
        cnt[i+1] -= 1
        cnt[i+2] -= 1
        continue
    if cnt[i] > 2:
        triplet += 1
        cnt[i] -= 3
        continue
    i += 1

etime = time.time()
print("time = ", etime-stime)
if (run + triplet) > 1:
    print("Baby Gin")
else:
    print("Fail")