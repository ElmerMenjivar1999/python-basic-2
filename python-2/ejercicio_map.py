my_list = [1,2,3,4,5]

def elevation(value):
    return value ** 2 - 1

print(list(map(elevation,my_list)))