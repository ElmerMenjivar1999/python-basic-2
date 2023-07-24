my_dictionary = {
    "name":"Elmer",
    "lastname":
    "Menjivar",
    "age":24}

def dictionary(dict:dict,key:str):
    try:
        return dict[key]
    except KeyError as Error:
        return Error
    

print(dictionary(my_dictionary,"age")) 

print(my_dictionary)

