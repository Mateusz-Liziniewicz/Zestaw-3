n=16
m=2
j=0
i=0
k=0
while(j<=m):
    while(i<=n):
        if(i%4==0):
            print("+", end="")
        else:
            print("-", end="")
        i+=1
    print()
    if(j!=m):
        while(k<=n):
            if(k%4==0):
                print("|", end="")
                k+=1
            else:
                print(" ", end="")
                k+=1
    print()
    i=0
    k=0
    j+=1