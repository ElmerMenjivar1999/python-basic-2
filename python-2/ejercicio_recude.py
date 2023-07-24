from functools import reduce
numbers = [1,2,3,4,5]

def union_word(number,other_number):
    return number + other_number

print(reduce(union_word,numbers))
