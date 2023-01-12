n=int(input("enter number between 1 and 10^9"))
a=str(n)
for i in range(0,len(a)):
    d=n%10
    n=n/10
    print(int(d))
