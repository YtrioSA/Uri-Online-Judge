# -*- coding: utf-8 -*-

n, words, wds = 1 , [], []
teste=""
while True:
    n, zera = int(input()), []
    if n == 0:
        break
    for w in range(n):
        word=input()
        words.append(word)
        zera.append(word)
    if n:
        wds.append(zera)

for i in range(len(wds)):
    max_word,output = max(map(len, wds[i])), ""
    for j in wds[i]:
        output += (max_word-len(j))*" "+j+"\n"
    teste += output  + "\n"
print(teste.rstrip())

