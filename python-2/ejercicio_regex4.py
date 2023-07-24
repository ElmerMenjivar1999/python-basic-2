import re

my_string = "Hola soy el profesor de matematicas , Mi nombre es = Roberto Contreras"

print(my_string)

separator = input("Caracter para dividir el string: ")

print(re.split(separator,my_string,re.I))

lista = ["tal","tal","tal","no","no"]
print(lista.count("tal"))