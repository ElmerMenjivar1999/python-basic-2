
num = int(input("Digite un numero de la tabla: "))

print(f"La tabla del {num}".center(5,"*"))
tabla_multiplicar = [num * i for  i in range(1,11)]
print(tabla_multiplicar)