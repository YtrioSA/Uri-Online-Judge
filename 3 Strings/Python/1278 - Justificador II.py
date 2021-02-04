# -*- coding: utf-8 -*-
teste=""
while True:
    n,frases,maior,nome=int(input()),[],[],""
    if n == 0:
        break

    # Frases
    for f in range(n):
        frases.append((input().upper()).split())


    for item in range(len(frases)):
        frase=""
        for j in frases[item]:
            frase += j+" "
        frases[item]=frase.strip()
        maior.append(len(frases[item]))

    # Alinhamento
    maior=max(maior)
    for i in range(len(frases)):
        rjust=maior-len(frases[i])
        nome += (rjust*" ")+frases[i]+"\n"
    teste += nome+"\n"
print(teste.rstrip())
