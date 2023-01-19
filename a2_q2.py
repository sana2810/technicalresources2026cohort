n=int(input("enter number of terms"))
for i in range(0,n):
    for j in range(n-i):
        print("*", end="\t")
    print("\n")
