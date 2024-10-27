lista =  [[],[4],(1,2),[3,4],(5,6,7)]
suma = []
for seq in lista:
    suma += [sum(seq)]
print(f"{suma} ", end="")