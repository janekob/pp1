from random import randint
liczba = int(input('Podaj liczbę od 1 do 6: '))
komp = randint(1,6)
print('komputer wyrzucił ',komp)
if komp == liczba:
    print:('wygrałeś')
else:
    print('przegrałeś')