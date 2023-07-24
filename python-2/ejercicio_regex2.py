import re

texto = "Hola a todos , mi nombre es elmer menjivar"

def search_word(text,chain_words):
    rango = re.search(text,chain_words,re.I)
    start,end = rango.span() 
    print(chain_words[start:end])
    return rango

result =search_word("todOs",texto)
print(result)
