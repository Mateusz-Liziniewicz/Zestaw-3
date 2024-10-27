n = 100
i=0
j=1
while(i<=n):
    if(i%5==0):
        print(f"|", end="")
        j+=1
    else:
        print(".", end="")
    i+=1
print()
k=1
l=0
while(l<=n):
    if(l%5==0):
        if(k!=9):
            print(f"{k:<5}", end="")
        else:
            print(f"{k:<4}", end="")
        k+=1
    l+=1
