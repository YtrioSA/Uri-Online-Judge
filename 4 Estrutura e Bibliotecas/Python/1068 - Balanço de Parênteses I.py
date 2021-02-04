# -*- coding: utf-8 -*-
while True:
    try:
        entrada,e = input(),""
        for x in entrada:
            if x == "(" or x == ")":
                e+=x
        entrada=e
        while entrada.count("()") != 0:
            entrada=entrada.replace("()","", 1)
        if entrada == "":
            print("correct")
        else:
            print("incorrect")
    except EOFError:
        break
