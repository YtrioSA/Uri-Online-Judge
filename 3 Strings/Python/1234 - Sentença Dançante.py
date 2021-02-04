# -*- coding: utf-8 -*-

while True:
    try:
        T = input()
        K = [lambda t: t.upper(), lambda t: t.lower()]
        C, A = 0, []
        for i in range(len(T)):
            A.append(T[i])
            if K[C](T[i]) != " ":
                A[i] = K[C](T[i])
                if C == 0:
                    C = 1
                else:
                    C = 0
        print("".join(A))
    except EOFError:
        break
