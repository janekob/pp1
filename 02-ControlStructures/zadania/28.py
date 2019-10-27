a=int(input('Wprowadź długość boku a: '))
b=int(input('Wprowadź długość boku b: '))

for x in range(a):
    for y in range(b):
        if x==0 or x==a-1:
            print('*',end='')
        elif y==0 or y==b-1:
            print('*', end='')
        else:
            print(' ',end='')
    print('')