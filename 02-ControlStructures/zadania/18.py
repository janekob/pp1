for x in range(31):
    if(x%3==0 and not x%5==0):
        print("three")
    elif(x%5==0 and not x%3==0):
        print("five")
    elif(x%3==0 and x%5==0):
        print('bingo')
    else:
        print(x)