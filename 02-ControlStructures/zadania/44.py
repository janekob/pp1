limit=int(input('podaj limit prędkości(km/h): '))
v=int(input('podaj prędkość samochodu(km/h): '))

if limit-v<10:
    mandat=(v-limit)*5
else:
    mandat=50+(v-limit-10)*15
print('mandat: ', mandat, 'zł') 