#Tipos de errores

#SyntaxError

#print "Hola comunidad" error
print ("Hola comunidad")

#NameError
name = 'elmer' #error, la variable no esta definida
print(name)

#IndexError
my_list = ["Python","Swift","Kotlin","Dart","JavaScript"]
print(my_list[4])
print(my_list[0])
#print(my_list[5]) error, indice fuera de rango de la lista

#ModuleNotFoundError
#import maths El modulo no existe
import math

#AttributeError

#print(math.PI) Error el atributo PI no existe en math, existe pi
print(math.pi)

#KeyError
my_dict = {"Nombre":"Elmer","Apellido":"Menjivar","Edad":24,1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) La key no existe en el diccionario


#TypeError

#print(my_list["0"]) acceder con el tipo de dato incorrecto
#my_list necesita un tipo de dato entero o slice no string
print(my_list[0])


#ImportError
#from math import PI no se puede importar PI no existe en math
from math import pi
print(pi)

#ValueError
my_int = int("10")
#my_int = int("10 Anios") No se puede convertir una cadena de texto a entero

print(type(my_int))

#ZeroDivisionError
print(4/2)
#print(4/0) no se puede dividir por 0
