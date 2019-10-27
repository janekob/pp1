import random

wynik = [random.randint(1,6) for x in range(100)]

print('szóstka: ', wynik.count(6))
print('piątka: ', wynik.count(5))
print('czwórka: ', wynik.count(4))
print('trójka: ', wynik.count(3))
print('dwójka: ', wynik.count(2))
print('jedynka: ', wynik.count(1))