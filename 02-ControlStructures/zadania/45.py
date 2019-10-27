N=int(input('Wprowadź ilość początkowych liczb pierwszych: '))
tab=[]
n=2
while len(tab)<N:
    for x in range(2,n):
        if (n%x)==0:
            break
    
    else:
        tab.append(n)
    n+=1
        
print('Liczby pierwsze: ',tab)
