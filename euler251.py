



def cardano(a,b,c):
    if ((a+b*(c**(1/2)))**(1/3))+((a-b*(c**(1/2)))**(1/3))==1:
        return 1
    else:
        return 0


print(cardano(2,1,5))
