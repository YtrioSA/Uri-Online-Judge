# -*- coding: utf-8 -*-
fc = list(map(int, input().split()))
v  = list(map(int, input().split()))
c  = list(map(int, input().split()))

fun,cli=fc[0],fc[1]
fila=c[fun:cli]
x=[v[i]*c[i] for i in range(fun if fun<cli else cli)]
n,l=0,len(fila)

while n < l:
    menor=min(x)
    index=x.index(menor)
    x[index]=x[index] - menor
    inmenor=x.index(0)
    x[inmenor] += menor + fila[n]*v[inmenor]
    n+=1
print(max(x))

