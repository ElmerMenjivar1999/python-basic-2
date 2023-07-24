import json
json_file = open("json_test.json","w+")
json_test = {
    "Nombre":"Alejandro",
    "Direccion":"Avenida Portugal",
    "Salario":15000,
    "Paises visitados":["Eslovaquia","Francia","Portugal"]
}
json.dump(json_test,json_file,indent=2)
json_file.close()
json_file = open("json_test.json")
json_print = json.load(json_file)#leyendo el json
print(json_print)

with open("json_test.json") as json_lines:
    for line in json_lines.readlines():
        print(line)

print(json_print["Nombre"])


