nombres = ["Alberto","Alba","Alejandro","Pablo","Ernesto","Elias"]
#filtrando los nombres que comiencen con la letra "A"
def name_start_with(value):
    return  value.startswith("A")

print(list(filter(name_start_with,nombres)))