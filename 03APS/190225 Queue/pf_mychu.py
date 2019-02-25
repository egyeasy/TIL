# 임의로 써봄
# candis = 20
# q = [i for i in range(20)]
# f = 0
# r = 0
# nextsn = 2
# studcan = [1] * 21


    
while candis > 0:
    f += 1; sn = q[f]
    candis -= studcan[sn]
    studcan[sn] += 1

    if candis <= 0:
        print("%d번 학생이 마지막 사탕을 받아간다."%sn)
        break

    r += 1; q[r] = sn
    r += 1; q[r] = nextsn

    nextsn += 1