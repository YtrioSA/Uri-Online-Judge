# -*- coding: utf-8 -*-

while True:
    
    hs  = input().split()
    H1  = int(hs[0])
    M1  = int(hs[1])
    H2  = int(hs[2])
    M2  = int(hs[3])

    if H1 == 0 and M1 == 0 and H2 == 0 and M2 == 0:
        break
    
    HM1 = (((24 if H1==0 else H1)*60)+M1)
    HM2 = (((24 if H2==0 else H2)*60)+M2) 
    
    if HM1 < HM2:
        print ( HM2 - HM1 )
    elif HM1 >= HM2:
        print( (24*60) - abs( HM2 - HM1 ) )
