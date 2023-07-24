import re

#RegEx personalizadas
my_strting = "Esta es la leccion numero 7: Leccion llamada Expresiones Regulares"
#definiendo un patron
pattern = r'[lL]eccion' #buscando la palabra leccion con la L minuscula o mayuscula
print(re.findall(pattern,my_strting))
#con | podemos poner mas patrones
pattern = r"[lL]eccion|Expresiones"
print(re.findall(pattern,my_strting))
#Buscando todas las palabras de la a a la z en minuscula
pattern = r"[a-z]"
print(re.findall(pattern,my_strting))
#Buscando solo numeros
pattern = r"[0-9]"
print(re.findall(pattern,my_strting))
#Solo tiene en cuenta los caracteres numericos
pattern = r"\d"
print(re.findall(pattern,my_strting))
#solo tiene en cuenta los caracteres no numericos
pattern = r"\D"
print(re.findall(pattern,my_strting))
#buscar coincidencias con la letra inicialmente
pattern = r"[l]."
print(re.findall(pattern,my_strting))
#Encuentra todo los caracteres a partir de la primera letra especificada
pattern = r"[l].*"
print(re.findall(pattern,my_strting))
email = "elmermenjivar48@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

print(re.match(pattern,email))
print(re.search(pattern,email))
print(re.findall(pattern,email))