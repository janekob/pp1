wers=int(input('Wprowadź liczbę wierszy: '))
if wers%2==0:
    srodek=int(wers/2)
else:
    srodek=int((wers+1)/2)
for x in range(srodek+1):
    for y in range(x):
        print('*',end='')
    print('')
for x in range(srodek,0,-1):
    for y in range(x):
        print('*',end='')
    print('')