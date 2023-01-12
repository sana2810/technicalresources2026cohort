low=int(input("enter lower value"))
high=int(input("enter higher value"))
print("prime numbers are:")
for i in range(low,high+1):
    
    for x in range(2,i):
        if i%x==0:
           
            break
        else:
            print(i)
            break
