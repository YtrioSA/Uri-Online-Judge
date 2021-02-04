# -*- coding: utf-8 -*-
m,k=True,len
for x in range(int(input())):print(" ".join(sorted(input().split(), key=k, reverse=m)))
