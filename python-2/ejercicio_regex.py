import re

texto = "Hola Usuario, Como estas?"
print(texto)
texto_usuario = input("Digite una oracion del texto para saber el rango donde se encuentra: ")
if texto_usuario != str(texto_usuario):
    print("Por favor digite una cadena de texto")
if texto_usuario == None:    
    match = re.match(texto_usuario,texto)
    rango = match.span()
    print(f"El rango se encuentra entre {rango}")
