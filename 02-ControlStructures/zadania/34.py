pesel=input('Wprowadź PESEL: ')
if len(pesel)==11:
    if int(pesel[9])%2==0:
        print('płeć: Kobieta')
    elif int(pesel[9])%2!=0:
        print ('płeć: Mężczyzna')
    if int(pesel[2:4])<=12:    
        wiek=(100- int(pesel[0:2]))+19
    elif int(pesel[2:4])>12: #dla osób urodzonych po 2000 roku
        wiek=19-int(pesel[0:2])
    print('wiek: ',wiek)
elif len(pesel)!=11:
    print('wprowadź poprawny numer pesel')
