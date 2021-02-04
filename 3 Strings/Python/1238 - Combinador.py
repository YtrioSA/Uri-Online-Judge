# -*- coding: utf-8 -*-

cases=int(input())
msg=''
for i in range(0, cases):
    mapStr = list(map(str, input().split(" ")))
    Array1 = [h1 for h1 in mapStr[0]]
    Array2 = [h2 for h2 in mapStr[1]]
    mStr   = min(len(Array1), len(Array2))
    for index in range(mStr):
       msg += Array1[index]+Array2[index]
    if len(Array1)>len(Array2):
        msg += "".join(Array1[mStr:max(len(Array1), len(Array2))])
    else:
        msg += "".join(Array2[mStr:max(len(Array1), len(Array2))])
    print(msg)
    msg=""
