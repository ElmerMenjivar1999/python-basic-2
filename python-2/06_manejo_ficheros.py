#Manejo de ficheros
import os
# .txt file
#r = lectura
#w = escritura
#w+ = escritura mas demas cosas, leer y escribir[Sobreescribe el fichero]
#r+ = Leer y escribir sin sobreescribir el fichero
#txt_file = open("./my_file.txt","r+")
#print(txt_file.read()) #Leyendo el fichero
#print(txt_file.read(10)) #Leyendo los 10 primeros caracteres
#print(txt_file.readline()) #Leyendo de linea en linea
#print(txt_file.readline())
#print(txt_file.readlines()) #Leyendo el fichero todas las lineas convirtiendola en una lista
txt_file = open("my_file.txt","w+")#Si no existe el fichero, lo crea
txt_file.write("Mi nombre es Elmer\nMi apellido es Menjivar\n24 anios\nMi lenguaje favorito es C++")
for element in txt_file.readlines():
    print(element)
#Escribiendo en el fichero
txt_file.write("\nAunque tambien me gusta kotlin")
txt_file.close()

with open("my_file.txt","a") as my_other_file:
    my_other_file.write("\nY Swift")

#os.remove("my_file.txt") Eliminando el fichero con el modulo os

#.json file
#Trabajar con archivos json
import json
json_file = open("my_file.json","w+")
json_test = {
    "name":"Elmer",
    "surname":"Menjivar",
    "age":24,
    "Language":["Python","Swift","Kotlin"],
    "website":"https://menjivar.dev"}
#Enviando informacion al son
#parametro 1 = informacion que se va a enviar,parametro 2 = nombre del archivo 
#indent = identacion del json
json.dump(json_test,json_file,indent=2)
#hay que cerrar el archivo para leerlo
json_file.close()

with open("my_file.json") as my_other_json:
    for line in my_other_json.readlines():
        print(line)
json_file = open("my_file.json")
#Leer un json con load, hay que abrir el archivo con open
json_dict = json.load(json_file)
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

#.csv file
import csv
csv_file = open("my_csv.csv","w+")
csv_write = csv.writer(csv_file)
#primera fila
csv_write.writerow(["name","surname","age","Language","website"])
csv_write.writerow(["Elmer","Menjivar",24,"Python","https://menjivar.dev"])
csv_file.close()
#xlsx file
#import xlrd debe instalarse el modulo
#XML file
import xml

