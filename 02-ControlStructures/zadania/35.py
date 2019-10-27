import math
a=float(input('Wprowadź wartość a: '))
b=float(input('Wprowadź wartość b: '))
c=float(input('Wprowadź wartość c: '))

delta=float(b**2-4*a*c)

if delta <0:
    print('delta ujemna')
    print('Funkcja nie ma trywialnych miejsc zerowych.')
if delta ==0:
    x= -b/2*a
    print('delta wynosi: ',delta)
    print('miejsce zerowe: ',x)
if delta >0:
    x_1=(-b+math.sqrt(delta))/2*a
    x_2=(-b-math.sqrt(delta))/2*a
    print('delta wynosi: ',delta)
    print('pierwsze miejsce zerowe: ',x_1)
    print('drugie miejsce zerowe: ',x_2)
    