import time

def isGin(nums):
    res = 0
    if nums[0] == nums[1] == nums[2] :
        res += 1
    if nums[0] == nums[1]+1 == nums[2]+2 :
        res += 1

    if nums[3] == nums[4] == nums[5] :
        res += 1
    if nums[3] == nums[4]+1 == nums[5]+2 :
        res += 1

    return res//2

#arr = [1,2,4,7,8,3]
#arr = [6, 6, 7, 7, 6, 7];
#arr = [0, 5, 4, 0, 6, 0];
arr = [1, 0, 1, 1, 2, 3];

perm = [0]*6
win = 0

stime = time.time()
L =len(arr)
for k1 in range(L):
    perm[0] = arr[k1]
    for k2 in range(L):
        if k2 != k1:
            perm[1] = arr[k2]

            for k3 in range(L):
                if k3 != k1 and k3 != k2:
                    perm[2] = arr[k3]
                    for k4 in range(L):
                        if k4 != k1 and  k4 != k2 and k4 != k3:
                            perm[3] = arr[k4]
                            for k5 in range(L):
                                if k5 != k1 and k5 != k2 and k5 != k3 and k5 != k4:
                                    perm[4] = arr[k5]
                                    for k6 in range(L):
                                        if k6 != k1 and k6 != k2 and k6 != k3 and k6 != k4 and k6 != k5:
                                            perm[5] = arr[k6]
                                            #print(perm)
                                            if isGin(perm) :
                                                win = 1
etime = time.time()
print("time : ", etime - stime)
import itertools

stime = time.time()
perm = list(itertools.permutations(arr))
for i in range(len(perm)):
    temp = list(perm[i])
    for j in range(len(temp)):
        if isGin(temp):
            win = 1

etime = time.time()
print("time : ", etime - stime)

if win : print("Baby-Gin")
else: print("not Baby-Gin")

