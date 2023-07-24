#Lambdas
#Es una funcion con la particularidad de que es anonima

sum = lambda first_value,seccond_value: first_value + seccond_value
print(sum(2,4))

multiply_values = lambda first_value,seccond_value: first_value*seccond_value - 3
print(multiply_values(2,6))
#Se puede combinar con una funcion normal
def sum_values(value):
    return lambda first_value,second_value:first_value + second_value + value
print(sum_values(5)(2,4))