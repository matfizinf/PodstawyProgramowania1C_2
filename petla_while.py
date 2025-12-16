#Pętla while - przykłady
from time import sleep

liczba = 120
licznik = 0

#W pętli while podajemy warunek TRWANIA pętli
while liczba > 0: #tak długo jak liczba jest dodatnia, pętla się wykonuje
    liczba = liczba // 2
    licznik = licznik + 1

print(licznik)

#Zadanie 1.
'''x = input('Podaj liczbę lub q aby zakończyć')
licznik = 0
while x != 'q':
    liczba = int(x)
    if liczba < 2:
        licznik = licznik + 1
    x = input('Podaj liczbę lub q aby zakończyć')
print(licznik)'''

#Zadanie 2.
'''popr_haslo = 'informatyka'
haslo = input('Podaj hasło')
proba = 1
while haslo != popr_haslo and proba < 5:
    print('Błędne hasło, podaj raz jeszcze!')
    haslo = input('Podaj hasło')
    proba = proba + 1

if haslo == popr_haslo:
    print('Witaj w systemie :)')
else:
    print('Nie ma hasła - nie ma dostępu')'''

from random import randint
#Zadanie 6.
'''wynik1 = 0
wynik2 = 0
akcja = 0

while not ((wynik1 >= 21 or wynik2 >= 21) and abs(wynik1 - wynik2) >= 2): #abs(x) = |x|
    akcja += 1 #akcja = akcja + 1
    print(f'Akcja {akcja}')
    #druzyna = int(input('Podaj nr drużyny, która wygrała akcję'))
    druzyna = randint(1, 2)
    if druzyna == 1:
        wynik1 += 1
    else:
        wynik2 += 1
    print(f'Wynik {wynik1} : {wynik2}')
    sleep(1)

if wynik1 > wynik2:
    print('Wygrała drużyna 1')
else:
    print('Wygrała drużyna 2')'''

#Zadanie 7.
'''liczba = int(input('POdaj liczbę'))

while liczba > 0:
    cyfra = liczba % 10
    liczba = liczba // 10
    print(cyfra, end = '')'''

#Zadanie 8.
liczba = int(input('Podaj liczbę'))
d = 2
ile_czyn = 0
ile_r_czyn = 0
while liczba > 1:
    if liczba % d == 0:
        ile_r_czyn += 1
    while liczba % d == 0:
        liczba = liczba // d
        ile_czyn += 1
    d += 1
print(ile_czyn)
print(ile_r_czyn)