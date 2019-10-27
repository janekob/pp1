import math
wzrost = float(input('Podaj wzrost w metrach: '))
masa = float(input('Podaj masę w kg: '))
BMI = masa/(wzrost**2)

print('Twoje BMI wynosi: ', BMI)

if BMI<18.5:
    print('niedowaga')
if BMI>= 18.5 and BMI <= 24.9:
    print('waga prawidłowa')
if BMI>=25 and BMI <=29.9:
    print ('nadwaga')
if BMI>30:
    print ('otyłość')
    
