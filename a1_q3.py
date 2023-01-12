t=int(input("enter the number of numbers to be checked for prime number between 1 and 10000 "))
for i in range(0,t):
    a=int(input("enter number between 2 and 10^9"))
    for x in range(2,a):
        if a%x==0:
            print("not prime")
            break
        else:
            print("prime number")
            break
