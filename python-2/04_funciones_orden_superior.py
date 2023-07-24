#Funciones de order superior

#son funciones que estan dentro de otras funciones
from functools import reduce #Para usar reduce
def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_one(first_value,second_value,sum_one):
    return sum_one(first_value+second_value)

print(sum_two_values_and_one(5,2,sum_one))
print(sum_two_values_and_one(5,2,sum_five))

#Clusures
#
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add
add_closure = sum_ten(1)
print(add_closure(5))
print(sum_ten(5)(1))

#Funciones de orden superior que existen en python
#Map siempre necesita un dato iterable
numbers = [2,5,10,21,3,30]
def multiply_two(number):
    return number * 2
print(list(map(multiply_two,numbers)))
print(list(map(lambda number:number * 2,numbers)))

#Filter necesita una funcion que retorne true o false
def filter_greater_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_ten,numbers)))
print(list(filter(lambda number:number > 10,numbers)))

#Reduce
def sum_two_values(first_value,second_value):
    return first_value + second_value 

print(reduce(sum_two_values,numbers))