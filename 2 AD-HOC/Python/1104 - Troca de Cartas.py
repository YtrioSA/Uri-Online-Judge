# -*- coding: utf-8 -*-

# 20:00
while True:
  try:
      
    # Número de cartas  
    cards = input().split()
    
    if int(cards[0])==0 and int(cards[1]) == 0:
        break
    
    cardsA = int(cards[0])*[0]
    cardsB = int(cards[1])*[0]
    
    k,f=input().split(),input().split()
    for cardA in range(0, len(k)):
        cardsA[cardA]=k[cardA]
    
    for cardB in range(0, len(f)):
        cardsB[cardB]=f[cardB]
    
    a=set(list(map(int, cardsA))) 
    b=set(list(map(int, cardsB)))

    #Intesecção A e B
    Iab=a.intersection(b)

    #Trocas
    m1=(len(a)-len(Iab)) 
    m2=(len(b)-len(Iab))
    print(min(m1, m2))
    
  except EOFError:
    break
