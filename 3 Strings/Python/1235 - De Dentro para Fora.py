
# -*- coding: utf-8 -*-
def simetria(x):
    (y,h)=(len(x)//2, len(x))
    (a,b)=(x[0:y][::-1],x[y:h][::-1])
    return a+b

for i in range(0, int(input())):
    print(simetria(input()))
