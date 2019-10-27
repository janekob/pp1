import math
a = float(input('podaj długość boku a: '))
b = float(input('podaj długość boku b: '))
c = float(input('podaj długość boku c: '))
p = (a+b+c)*(1/2)
S = math.sqrt(p*(p-a)*p*(p-b)*(p-c))
print ('obwód trójkąta wynosi: ', S)