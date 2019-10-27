tab=['Genowefa','Onufry','Celestyna','Alojzy','Pankracy','Teofil']
index = None
maks=0
for n in tab:
    if len(n)> maks:
         maks=len(n)
         index=tab.index(n)
         
print('najdłuższe imię w tabeli, to: ',tab[index])