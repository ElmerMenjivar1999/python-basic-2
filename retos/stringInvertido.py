def reverse(text):
    len_text = len(text) 
    variable = ""
    for i in range(0,len_text):
        variable += text[len_text - i - 1]
    return variable

print(reverse("Hola mundo"))


