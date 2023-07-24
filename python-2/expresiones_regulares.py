#Expresiones regulares
#regular expression
import re
#match
my_strting = "Esta es la leccion numero 7: Leccion llamada Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de ficheros"
match = re.match("Esta es la leccion",my_strting,re.I)
print(re.match("Esta es la leccion",my_strting))#Comprobando si una oracion esta en una variable
print(re.match("Esta es la leccion",my_other_string))

print(re.match("Expresiones Regulares",my_strting))
#Con match empieza a buscar desde el principio
print(match)
#Desempaquetando el span en 2 variables , una inicial y otra final
start,end = match.span()
print(my_strting[start:end]) #Imprime solo el rango

#search busca palabras u oraciones en concreto

search = re.search("leccion",my_strting,re.I)
print(search)
start,end = search.span()
print(my_strting[start:end])

#findall = cuenta las palabras especificadas que se encuentran en el string
#en forma de una lista []
#re.I ignora si la palabra esta en minuscula o mayuscula
findall = re.findall("leccion",my_strting,re.I)
print(findall)


#Split buscar un patron y divide a partir del patron especificado en forma de lista[]
print(re.split(":",my_strting))

#sub- substituye las palabras por otra palabra especificada
#solo toma en cuenta el valor inicial, si hay repetidos no sustituye todos
print(re.sub("Expresiones","expresiones",my_strting))
print(re.sub("Expresiones Regulares","RegEx",my_strting))
#| se aplica a las dos palabras
print(re.sub("leccion|Leccion","LECCION",my_strting))

