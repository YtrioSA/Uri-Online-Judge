# -*- coding: utf-8 -*-

n=int(input())
for c in range(n):
    d,diamantes=input().replace(".",""),0
    while d.count("<>") != 0:
        d=d.replace("<>","", 1)
        diamantes+=1
    print(diamantes)
