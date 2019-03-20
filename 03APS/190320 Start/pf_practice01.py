arr = ""

t = 0
for i in range(len(arr)):
    t = t * 2 + int(arr[i])
    if i + 1 % 7 == 0:
        print(t, end=" ")
        t = 0