#1. Wprowadzanie danych przez użytkownika do programu
from zmienne import liczba_z_przecinkiem

#1) utworzenie zmiennej
#2) na ekranie pojawia się komunikat z inputa
#3) program się zatrzymuje i czeka na podanie danych i zatwiedzenie tego ENTEREM
#4) po wpisaniu i zatwierdzeniu ENTEREM to co wpiszemy trafia jako string do zmiennej
#5) i program wykonuje się dalej
imie = input('Podaj swoje imię')

liczba = int(input('Podaj liczbę'))
print(type(liczba))

liczba_z_przecinkiem = float(input('Podaj liczbę z przecinkiem'))
print(type(liczba_z_przecinkiem))

cos = list(input('Podaj coś'))
print(cos)
print(type(cos))