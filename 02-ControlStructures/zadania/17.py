parzyste=0
nieparzyste=0
for n in range(2,51,2):
    parzyste=parzyste+n
for n in range(1,50,2):
    nieparzyste=nieparzyste+n
print('suma parzystych wynosi: ', parzyste)
print('suma nieparzystych wynosi: ',nieparzyste)