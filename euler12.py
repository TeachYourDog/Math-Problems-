

#Generates list of triangle numbers
number = 0
list=[]
for i in range(1,10000000):
  number = number + i
  if number%2==0:
    list.append(number)


#Finds all divisors of each number
for i in range (1, len(list)):
    div=[]
    n=list[i]
    for i in range(1,n+1):
        if(n%i==0):
            div.append(i)

    if len(div) >= 100:
        print(str(len(div)) + 'and' + str(n))
