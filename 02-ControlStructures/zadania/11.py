login_M = 'marek'
haslo_M='m-123'
login = input('Podaj login: ')
haslo = input('Podaj haslo: ')

if login_M != login or haslo_M != haslo:
    print('Podane dane są nieprawidłowe')
    
else:
    print('Logowanie udane')