import time

st = time.time()
arr = '01D06079861D79F99F'

# arr = arr * 100000

arr = arr.replace('0', '0000')
arr = arr.replace('1', '0001')
arr = arr.replace('2', '0010')
arr = arr.replace('3', '0011')
arr = arr.replace('4', '0100')
arr = arr.replace('5', '0101')
arr = arr.replace('6', '0110')
arr = arr.replace('7', '0111')
arr = arr.replace('8', '1000')
arr = arr.replace('9', '1001')
arr = arr.replace('A', '1010')
arr = arr.replace('B', '1011')
arr = arr.replace('C', '1100')
arr = arr.replace('D', '1101')
arr = arr.replace('E', '1110')
arr = arr.replace('F', '1111')

t = 0
for i in range(len(arr)):
    t = t * 2 + int(arr[i])
    if (i+1) % 7 == 0:
        print(t, end=' ')
        t = 0

print(time.time() - st)
print()


st = time.time()
arr1 = '01D06079861D79F99F'

# arr1 = arr1 * 100000

table = [[0, 0, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 1, 0],
         [0, 0, 1, 1],
         [0, 1, 0, 0],
         [0, 1, 0, 1],
         [0, 1, 1, 0],
         [0, 1, 1, 1],
         [1, 0, 0, 0],
         [1, 0, 0, 1],
         [1, 0, 1, 0],
         [1, 0, 1, 1],
         [1, 1, 0, 0],
         [1, 1, 0, 1],
         [1, 1, 1, 0],
         [1, 1, 1, 1]]

arr = [0] * (len(arr1)*4)

for i in range(len(arr1)):
    if arr1[i] <= '9':
        idx = ord(arr1[i]) - ord('0')
    else:
        idx = ord(arr1[i]) - ord('A') + 10
    for j in range(4):
        arr[i * 4 + j] = table[idx][j]

t = 0
for i in range(len(arr)):
    t = t * 2 + int(arr[i])
    if (i+1) % 7 == 0:
        print(t, end=' ')
        t = 0
print(time.time() - st)
