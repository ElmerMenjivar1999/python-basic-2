def saludo():
    def name(name):
        return f"Hola {name}, como estas?"
    return name

usuario = saludo()
print(usuario("Elmer"))

def list_number(value):
    def pares(other_value):
        return other_value + value
    return pares

lista = list_number([1,2,3])
print(lista([4,5,6]))
