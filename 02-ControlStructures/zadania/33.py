nazwy=['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']
cyfra=(input('podaj liczbę: '))
for n in cyfra:
    print(nazwy[int(n)], ' ',end='')
    