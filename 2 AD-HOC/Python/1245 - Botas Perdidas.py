# -*- coding: utf-8 -*-
while True:
  try:
    Numbers=[]
    Lista=[]
    for i in range(int(input())):
       Input=input().split()
       Lista.append(''.join(Input))
       Numbers.append(Input[0])
    
    seach=[]
    for x in set(Numbers):
        for j in ['E', 'D']:
            seach.append(x+j)
    item=0
    pares=0
    for i in range(int((len(seach)/2))):
        Tda=Lista.count(seach[item])
        Tdb=Lista.count(seach[item+1])
        pares+=min(Tda, Tdb) 
        item=(item+2)
    print(pares)
  except EOFError:
    break
