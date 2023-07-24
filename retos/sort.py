n = [3,4,1,2,5 ,10,0,6]
aux = 0
longitud = len(n)
for i in range(longitud):
    for j in range(longitud - 1):
        if n[j] > n[j+1]:
            aux = n[j]
            n[j] = n[j+1]
            n[j+1] = aux

print(n)