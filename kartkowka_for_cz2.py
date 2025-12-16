'''n = int(input('Podaj liczbę'))

iloczyn = 1

for x in range(n):
    iloczyn = iloczyn * (x + 1)

print(iloczyn)'''

'''iloczyn = 1

for x in range(1, n + 1):
    iloczyn = iloczyn * x

print(iloczyn)'''

#Zadanie 2.
lista = [4, 12, 8, 1, 5, 6, 3]
licznik = 0

'''for x in range(len(lista)):
    for y in range(len(lista)):
        if lista[x] != lista[y] and (lista[x] + lista[y]) % 3 == 0:
            #print(lista[x], lista[y])
            licznik = licznik + 1
print(licznik)'''

'''for x in lista:
    for y in lista:
        if x != y and (x + y) % 3 == 0:
            #print(x, y)
            licznik = licznik + 1
print(licznik)'''

#Zadanie 3.
'''n = int(input('Podaj ile będzie napisów'))
max_napis = ''
for x in range(n):
    napis = input('Podaj napis')
    ile_a = napis.count('a')
    max_ile_a = max_napis.count('a')
    if ile_a > max_ile_a:
        max_napis = napis
print(max_napis)'''

#Zadanie 6.
