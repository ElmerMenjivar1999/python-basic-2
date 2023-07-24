import re

texto = "hola hola , que tal tal tal, mi nombre nombre es es es es Elmer"

print(re.findall("tal",texto,re.IGNORECASE))