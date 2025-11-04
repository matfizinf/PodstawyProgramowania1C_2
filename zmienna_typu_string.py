from itertools import repeat

napis = 'informatyka'

#I. Fragment tekstu:
#1) wycinanie od ... do
print(napis[2:5]) #czyli tak naprawdę od 2 do 4

#2) wycinanie od ... do co ileś
print(napis[2:10:2])

#3) wycinanie od początku
print(napis[:3])

#4) wycinanie do końca
print(napis[7:])

#5) czytanie od końca
print(napis[::-2])

#II. Zawieranie się znaku w słowie
if 'x' in napis:
    print('należy')
else:
    print('nie należy')

#III. Łączenie napisów (konkatenacja)
napis2 = napis + 'jestnajlepsza'
print(napis2)

#IV. Funkcje zmiennych typu string

#1) poszukiwanie danego fragmentu w tekście
napis3 = 'matematyka'
index_gdzie_jest = napis3.find('tem')
print(index_gdzie_jest)

napis4 = 'alabalalalabala'
index_gdzie_jest2 = napis4.find('bala')
index_gdzie_jest3 = napis4.find('bala', index_gdzie_jest2 + 1)
index_gdzie_jest4 = napis4.find('xyz', index_gdzie_jest2 + 1)
print(index_gdzie_jest2)
print(index_gdzie_jest3)
print(index_gdzie_jest4)

if napis4.find('xyz') != -1:
    print('xyz jest w napisie')
else:
    print('xyz nie jest w napisie')

#2.)Podział tekstu na fragmenty
'''piec_liczb = input('Podaj pięć liczb. Oddziel je przecinkiem')
piec_liczb_po_podziale = piec_liczb.split(',')
print(piec_liczb_po_podziale)
trzecia_liczba = int(piec_liczb_po_podziale[2])
print(trzecia_liczba + 33)'''

#3.) Łączenie napisów
lista_napisow = ['Windows', 'jest', 'tworzony', 'dla', 'kasy']
cale_zdanie = '@'.join(lista_napisow)
print(cale_zdanie)

lista_napisow2 = ['abc', 'xyz', 'bbc', 'tvn']
cale_zdanie2 = '\n'.join(lista_napisow2)
print(cale_zdanie2)

#4.) Zliczanie danego znaku w tekście
napis5 = 'prawdopodobieństwo'
ile_razy_o = napis5.count('o')
print(ile_razy_o)

#5.) "Mutowalność" stringów
napis6 = "fiwyka"
'''napis6[2] = 'z'
print(napis6)'''
#Wniosek: String są niemutowalne, czyli nie można podmieniać pojedynczych liter

#Sposób na zmutowanie stringa
napis6_lista = list(napis6)
print(napis6_lista)
napis6_lista[2] = 'z'
print(napis6_lista)
napis6 = ''.join(napis6_lista)
print(napis6)

#6) Długość napisu
napis7 = 'językpolski'
print(len(napis7))

#7) Powielanie stringa
napis8 = 'informatyka'
print(napis8 * 3)

#8) Funkcje testujące cyfry i litery
napis9 = 'qwerty1'
if napis9.isalpha() == True:
    print('słowo składa tylko się z liter')
else:
    print('słowo nie składa się z liter')

napis10 = '1410w'
if napis10.isdigit() == True:
    print('słowo składa tylko się z cyfr')
else:
    print('słowo nie składa się z cyfr')

napis11 = '1410w\n'
if napis11.isalnum() == True:
    print('słowo składa tylko się z cyfr lub liter')
else:
    print('słowo nie składa się tylko cyfr lub liter')