x=int(input('wprowadź pierwszą wartość: '))
y=int(input('wprowadź drugą wartość: '))
z=int(input('wprowadź trzecią wartość: '))

if y<x<z or y>x>z:
    print('mediana wynosi: ',x)
elif x<y<z or x>y>z:
    print('mediana wynosi: ',y)
else:
    print('mediana wynosi: ',z)
    