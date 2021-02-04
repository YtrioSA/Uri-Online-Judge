
# -*- coding: utf-8 -*-
n = int(input()) + 1
while (n-1)!=0:
    x = list(range(1, n))
    DiscardedCards=[]
    while len(x) != 1:
        DiscardedCards.append(x.pop(0)) # joga fora a carta do topo.
        x.append(x.pop(0)) # e move a próxima carta para a base da pilha.

    print("Discarded cards: "+", ".join(list(map(str, DiscardedCards))))
    print("Remaining card: "+str(x[0]))
    n = int(input()) + 1
