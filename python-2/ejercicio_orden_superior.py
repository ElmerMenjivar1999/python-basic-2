lista = [2,3,4,5]

def pow_number(value):
    return list(value) 

def lista_elevada(number_list,elevacion):
    return elevacion(number_list * 2)

print(lista_elevada(lista,pow_number))
