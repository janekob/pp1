tab=[15,8,31,47,2,19]
sum=0
dzielnik=0
for n in tab:
    if n%2!=0:
        sum+=n
        dzielnik+=1


print(sum/dzielnik)