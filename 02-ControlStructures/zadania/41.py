
dzielnik=0
liczba=float(input('Wprowadź liczbę: '))
suma=0
while liczba !=0:
    liczba=float(input('Wprowadź liczbę: '))
    
    suma+=liczba
    dzielnik+=1
    
    
print('Rezultat:')
print('liczb= ',dzielnik)
print('suma= ', suma)
print('średnia arytmetyczna: ', suma/dzielnik)