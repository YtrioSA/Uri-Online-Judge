# -*- coding: utf-8 -*-

l=[]
for x in range(1, int(input())+1):
    l.append(int(input()))

s=list(set(l))
s.sort()
for y in s:
    print("{} aparece {} vez(es)".format(y, l.count(y)))
