arr = '0269FAC9A0'

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

patt = ['001101', '010011', '111011', '110001',
        '100011', '110111', '001011', '111101',
        '011001', '101111']

for i in range(len(arr) - 6):
    if arr[i: i + 6] in patt:
        x = patt.index(arr[i: i + 6])
        break

print(arr)
for i in range(arr.index(patt[x]), len(arr) - 6, 6):
    print(patt.index(arr[i: i + 6]), end =' ')


