
# -*- coding: utf-8 -*-
def circularAlphabet(letter, dec):
    if (ord(letter)-dec) in list(range(65, 91)):
        return (chr(ord(letter)-dec))
    else:
        return (chr(91-(dec-(ord(letter)-ord('A')))))

testCases=int(input())
msg=''
for case in range(testCases):
    str=list(input())
    dec=int(input())
    for k in str:
        msg += circularAlphabet(k, dec)
    print(msg)
    msg=""

