text_file = open("file_text.txt","w+")
text_file.write("Hola mi nombre es Elmer\nY este es mi archivo de prueba")
#print(text_file.read())
# print(text_file.readline())
# print(text_file.readline())
#print(text_file.readlines())
text_file.write("\nMi lenguaje favorito es C++")
text_file.close()
text_file = open("file_text.txt","r+")
#print(text_file.read())
for element in text_file.readlines():
    print(element)

with open("file_text.txt","a") as other_file:
    other_file.write("\nY tambien Java")
print(text_file.read())
text_file.close()
