PIN='0805'

for n in range(3):
    kod=(input('Wprowadź PIN: '))
    if kod==PIN:
        print('kod poprawny')
        break
    else:
        print('Kod nieprawidłowy. Wprowadź ponownie.')
    if n ==2:
        print('karta zablokowana')
        break
    