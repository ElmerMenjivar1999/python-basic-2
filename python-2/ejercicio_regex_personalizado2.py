import re

texto = "Hola como estan?. Yo muy bien gracias. Sabes si @elmer esta conectado? Mi numero de telefono es 9998887726"

pattern = r"[a-zA-Z-0-9-?-@-.]"
find = re.findall(pattern,texto)
pattern = r"\d"
find = re.findall(pattern,texto)
pattern = r"\D"
find = re.findall(pattern,texto)
print(str(find))
