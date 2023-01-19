n=int(input("enter number of terms"))

for i in range(0,n):
    for s in range(0,i+1):
        print(" ",end="\t")
    for j in range(n-i):
        print("*",end="\t")
    print("\n")
