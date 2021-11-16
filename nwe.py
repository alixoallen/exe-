um=int(input('digite um valor : '))
dois=int(input('digite um valor : '))
tres=int(input('digite um valor : '))
quatro=int(input('digite um valor : '))
tup=(um,dois, tres, quatro)

tuplax = tup
cont = 0
print (f"Você digitou os valores {tup}")
for igual in tup:
    if igual == 9:
        cont += 1
print (f"O valor 9 apareceu {cont} vezes")
if 3 in tup:
    print(f"O número 3 apareceu na {tup.index(3)+1}º posição")
else:
    print ("Não contêm número 3 na tupla")

county = 0
countx = 0

for tuplax in tup:
    if tuplax % 2 == 0:
        county += 1
    else:
        countx += 1

print (f"Os valores pares digitados foram {county}")

