x=float(input('Wprowadź wartość x: '))
y=float(input('Wprowadź wartość y: '))
if x>0 and y>0:
    print('Punkt znajduje się w pierwszej ćwiartce układu współrzędnych.')
elif x>0 and y<0:
    print('Punkt znajduje się w czwartej ćwiartce układu współrzędnych.')
elif x<0 and y<0:
    print('Punkt znajduje się w trzeciej ćwiartce układu współrzędnych.')
else:
    print('Punkt znajduje się w drugiej ćwiartce układu wpółrzędnych.')